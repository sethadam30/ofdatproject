Developer's documentation
=========================

There are three ways to contribute to the OFDAT project:

* Checking/elaborating documentation, proposing features [&rarr;](#documentation)
* Forensic module development [&rarr;](#modules)
* OFDAT core development [&rarr;](#core)


Working on the documentation<a name="documentation"></a>
----------------------------

It is not necessary to be a bioinformatician to contribute to
OFDAT. Any programming project has to start with a specification of
what the program should be able to do. Having a clear specification,
will help to speed up the development. The specification should
contain everything forensic analysts will need to do with MPS data.
If you are a potential end-user and you know what you want to do with
MPS data, or you find that OFDAT is not processing the data
accordingly, contributing is as simple as sharing that information.

The documentation should also contain the same information when the
features of the specification are implemented. In OFDAT the
specification is made by making the documentation beforehand.
Depending on your experience in contributing to programming projects,
there are several ways to help out with this:

1. The easiest is to submit a *bug report* or *feature request* to the
issue tracker on GitHib
[&rarr;](https://github.com/OFDAT/ofdatproject/issues).

2. If the documentation does not match with how OFDAT operates, you
can change it directly by forking the project, changing the erroneous
paragraphs, and submitting a pull request.

3. Submit the documentation/specification for your *feature request*
with a pull request.

For all three ways you need to sign up as a GitHub user. Points 2 and
3 require forking OFDAT and submitting a pull request. In the top
right corner of the OFDAT main page
([&rarr;](https://github.com/OFDAT/ofdatproject)), click *Fork*. You
will then be in your own OFDAT fork. Go to the documentation page that
needs to be changed (e.g. `docs/docs/developers.md`). Click on the
*edit button* (to the right of *History*). Make your changes. Select
*Create a new branch for this commit and start a pull request* at the
bottom. Click on *Propose file change*. Optionally leave an extra
comment to clarify the proposed change. Finally, click on *Create pull
request*.

### Documentation conventions

The documentation system for OFDAT has several conventions that should
be respected when submitting a *pull request*. First, documentation
files are made with the Markdown markup language. It has a very
intuitive syntax and takes just 5 minutes to learn
([https://help.github.com/articles/markdown-basics/](https://help.github.com/articles/markdown-basics/)).
Second, when adding a specification to the documentation that is not
yet implemented, precede it with "[spec]". This way, readers of the
documentation now that it is about a future enhancement and not
something that already works.

If your *feature request* is for an API (something that other
bioinformaticians can use without a graphical interface), add a
documentation test or
*[doctest](https://docs.python.org/3/library/doctest.html)*. For
example:

    >>> from ofdat.LR.models import retrieveNumberOfContributors,testData # doctest: +SKIP
    ... retrieveNumberOfContributors(testData)
    4

When the feature is implemented, this doctest will then serve as an
example for the use of the API and an automated test that checks its
continued functioning in future OFDAT versions.


Forensic module development<a name="modules"></a>
---------------------------

The second way to contribute to OFDAT is by developing forensic
modules or tools. This can be done completely independently from the
OFDAT development itself, except for two requirements:

1. At the very minimum, the module needs a command-line interface
(CLI).
2. Documentation should be provided in the same format as OFDAT.

### CLI specification

OFDAT will track the user's execution of any module. The specific
command with which the module was executed will be logged. In order to
do that the CLI needs to be incorporated in the Django web
application. The CLI should be specified with the following xml structure:

    <?xml version="1.0" encoding="UTF-8"?>
    <tool id="toolExample" version="1.0.0" name="Example xml tool config">
     <description>
      A more elaborate description of the tool.
      This can be multiple lines and include *markdown*
     </description>
     <command interpreter="python">toolExample.py</command>
     <inputs>
      <argument name="--threshold" type="float" default="0.05"
      help="sets the threshold" nargs="*" />
      <argument 
     </inputs>
     <outputs>
     </outputs>

     <tests>
      <test>
      </test>
     </tests>
    </tool>

The general format of the xml has been derived from the
[Galaxy-project tool configuration
](https://wiki.galaxyproject.org/Admin/Tools/ToolConfigSyntax). Adaptations
have been made to work with Django. The *command* tags should only contain the
program name; *command* atttribute *interpreter* is only required for
interpreted scripts without a shebang. The argument types can be:

* int
* float
* str
* file

They are mapped to Django field types. The validity of the xml can be
tested as follows

    >>> from ofdat.tools.config import parseConfig
    ... parseConfig('documentationExample.xml',testValidity=True)
    True
    
### Integration within OFDAT



OFDAT core development<a name="core"></a>
----------------------
