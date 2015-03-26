Installation
============

Basic requirements
------------------
virtualenv
python3.4

Deployment documentation
------------------------
These are instructions on how to install the OFDAT platform outside of a container in a server environment.
TODO: server requirements

    mkdir ~/virtualenvs
    cd ~/virtualenvs
    git clone https://github.ugent.be/cvneste/ofdat.git ~/virtualenvs/ofdatproject
        #If askpass problem 'unset SSH_ASKPASS'
    git clone https://github.com/beukueb/pybbm.git ~/virtualenvs/pybbm #forum functionality
    virtualenv -p /usr/local/bin/python3.3 ~/virtualenvs/ofdatproject
    source ~/virtualenvs/ofdatproject/bin/activate
    pip install -r ~/virtualenvs/ofdatproject/requirements.txt
    mkdir ~/virtualenvs/ofdatproject/{static,media}
    cd ~/virtualenvs/ofdatproject/ofdat
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic
    python manage.py runserver 0.0.0.0:8000 #Test server

 ### Nginx setup
 
    cp /etc/nginx/uwsgi_params ~/virtualenvs/ofdatproject/ofdat/ofdat/
    cat > ~/virtualenvs/ofdatproject/ofdat/ofdat/nginx_ofdat.conf <<EOF
    	# nginx_ofdat.conf

	# the upstream component nginx needs to connect to
	upstream djangofdat {
		 server unix:///home/christophe/virtualenvs/ofdatproject/ofdat/ofdat/nginx_ofdat.sock; # file socket - amend as required
	         #server 127.0.0.1:8001; # web port socket
		 }

	# configuration of the server
	server {
    	       # the port your site will be served on
	       listen      80;
	       # the domain name it will serve for
	       server_name ofdat.van-neste.be; # substitute your machine's IP address or FQDN
	       charset     utf-8;

	       # max upload size
	       client_max_body_size 75M;   # adjust to taste

	# Django media
	    location /media  {
	             alias /home/christophe/virtualenvs/ofdatproject/media;  # your Django project's media files - amend as required
	    }

	    location /static {
	    	     alias /home/christophe/virtualenvs/ofdatproject/static; # your Django project's static files - amend as required
   	    }

    	# Finally, send all non-media requests to the Django server.
    	   location / {
           	    uwsgi_pass  djangofdat;
        	    include     /home/christophe/virtualenvs/ofdatproject/ofdat/ofdat/uwsgi_params; # amend as required
           }
	   }
    EOF
    #Amend for current installing user
    sed -i "s&/home/christophe&${HOME}&g" ~/virtualenvs/ofdatproject/ofdat/ofdat/nginx_ofdat.conf
    sudo ln -s ~/virtualenvs/ofdatproject/ofdat/ofdat/nginx_ofdat.conf /etc/nginx/conf.d/
    cat > ~/virtualenvs/ofdatproject/ofdat/ofdat/uwsgi_ofdat.ini <<EOF
        # uwsgi_ofdat.ini file
    	[uwsgi]
    
        # Django-related settings
    	# the base directory (full path)
    	chdir        = /home/christophe/virtualenvs/ofdatproject/ofdat/
	# Django's wsgi file
    	module       = ofdat.wsgi
    	# the virtualenv (full path)
    	home         = /home/christophe/virtualenvs/ofdatproject
    
        # process-related settings
    	# master
    	master       = true
	# maximum number of worker processes
	processes    = 10
	# the socket (use the full path to be safe
    	socket       = /home/christophe/virtualenvs/ofdatproject/ofdat/ofdat/nginx_ofdat.sock
    	# ... with appropriate permissions - may be needed
    	chmod-socket = 666
    	# clear environment on exit
    	vacuum       = true
    EOF
    #Amend for current installing user
    sed -i "s&/home/christophe&${HOME}&g"  ~/virtualenvs/ofdatproject/ofdat/ofdat/uwsgi_ofdat.ini
    
    #Test nginx setup
    ##Test that the socket directory is readable
    if ! sudo -u nobody ls ~/virtualenvs/ofdatproject/ofdat/ofdat then echo "Socket is not readable, fix the path"; fi
    ##Restart nginx to load ofdat configuration
    sudo service nginx restart
    ##Startup socket
    uwsgi --ini ~/virtualenvs/ofdatproject/ofdat/ofdat/uwsgi_ofdat.ini &
    ##Test that you can see the OFDAT homepage in your browser
    disown #Then it will not shutdown after logging out of the shell

### Supervisor setup

At this point the web app would already be functional, but the extra
processes such as uwsgi, would need to be started up manually after
each restart.

Assuming supervisord is installed `sudo apt-get install supervisord &&
sudo chkconfig supervisord on`, the following commands will automate
the startup of all necessary processes.

    cat >> /etc/supervisord.conf <<EOF
    
        [program:uwsgi]
	command=bash -c "source ~/virtualenvs/ofdatproject/bin/activate && uwsgi --ini ~/virtualenvs/ofdatproject/ofdat/ofdat/uwsgi_ofdat.ini"
	priority=888
	user=christophe

	[program:celery]
	command=bash -c "source ~/virtualenvs/ofdatproject/bin/activate && ~/virtualenvs/ofdatproject/bin/celery -A ofdat worker -l info"
	numprocs=1
	directory=/home/christophe/virtualenvs/ofdatproject/ofdat
	priority=999
	startsecs=10
	startretries=3
	user=christophe
	redirect_stderr=true
	stdout_logfile=/var/tmp/celery.log
    EOF

supervisord.conf still needed to be ammended with the following, as supervisorctl was not working:

    [unix_http_server]
    file=/var/tmp/supervisor.sock

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
