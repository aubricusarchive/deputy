# Notes

## My Problems with Yeoman
* gruntjs seems handy, but it requires node and i am not fond of how it handles configuration
    * need to investigate grunt a little bit more.
* perscriptive, though configurable though generators.
    * My problem with generators is that it requires me to 'learn' generators just to use them
    * Ultimately I'm sure the 'generator' concept allows a lot of flexibility, it seems like overkill when I just want to copy boiler plate.
    * Additionally, what the generator does, and how other processes are automated seem disconnected. 
        * It's possible I don't understand it, and that is why. 
        * But at the same time their system is not easily digested by those unfamiliar with grunt.js and ruby generators.
* will not run on vagrant
    * compass watch is broken when running process on a shared folder between a vm and the host machine
* yeoman api is a black box
    * I can't extend their api, aside from generators. 
    * When i do that i get really awful syntax like `yeoman init generator:BLAH`
    * Why can't I just write more tasks?
    * I'm sure its possible to write custom grunt tasks, but now I'm running things outside yeoman (bleh)
        * I'll admit i don't understand the whole system, could be wrong here.
* node requirement
    * writing tasks in fabric doesn't require node
    * a simple http server can be provided via python, and is just a python std lib.
    * i find node's syntax requirements cumbersome, and js is just not the most full featured language ever.
        * callback hell

## Goal
* To create a very extensible, non-perscriptive build tool.
    * Custom API should be easy to write / integrate.
    * Tool structure should be straight forward
* Provide basic automation, but leave final solution up to developer
    * Too many frameworks try to solve every conceivable use case
        * Because this is not possible, you have to create a somewhat rigid structure to solve "only a few" kinds of problems.
* Pieces should be removable
    * Don't like PhantomJS? Fine, replace the 'test' process with your own automation.
    * Plugin architecture.

## Software
* Sass (Ruby)
* Compass (Ruby)
* Bower (js, node)
* Fabric (Python)
* Optipng(c)
* JpegTran(c)
* Closure Compiler(Java)
* Docco (node, documentation)

## Python Setup
* cliff (cli)
* pdb++ (debugger)
* pdbSublimeTextSupport (pdb plugin for sublime)
* pycmd (code analytics)
* sphinx (documentation) http://sphinx-doc.org/
* pycco (documentation) http://fitzgen.github.com/pycco
* unittest, pytest, nose

## Planned Features:

### simple http server for quick development

### simple, extensible api (fabric? & or straight up python)

### automate
* server configuration (vagrant & puppet)
* build tasks
    * compress css
    * compress js (require / closure)
    * compress html
    * enforce code standards (linters)
    * image optimization (jpegtran, optipng)
* git tasks
    * master, release, preview, feature
* deployment
    * capistrano style with rollback
    * fpm with git / packaging
* cache busting
* unit testing
    * phantom js
    * mocha
    * qunit

### boilerplate
* editorconfig
* jsHint options
* file structure based boilerplate (like FlashDevelop)

### Front-End Package Management
* look at bower
    * not a huge requirement, it's not that hard to manage

### Random Thoughts
* Checkout Google Closure Tools
* Is there a way to provide a basic api, w/o providing a default structure?
    * Maybe that is "fabric" itself. 
    * And I won't get away from building at least a little bit of default functionality.
* Plugins? 
    * Plugin's would allow me to write implementation for n-tools but add a nice layer of abstraction. People can build plugins and adapt the system to whatever requirements they need.
    * That could be the 'core' of this thing.
        * Then my implementation is essentially example code that 'selects' a few common tools
    * check [this](http://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures/) out.

## Plugin System Notes

### Fundamental Plugin Concepts
1. Discovery
* Registration
* Application hooks to which the plugins attach (a.k.a 'mount points')
* Exposing application capabilities back to plugins (a.k.a. 'extension api');

#### Discovery
* This is the mechanism by which a running application can find out which plugins it has at its disposal.
* To "discover" a plugin, one has to look in certain places and also know what to look for.
* In our example - plugins are Python classes that inherit from a known base class contained in modules located in known places.
    * There are a few patterns here:
        * configuration file
        * known location
        * configuration file + known locations (?)

#### Registration
* This is the mechanism by which a plugin tells an application - "I'm here, ready to work".

#### Hooks
* Hooks are also called "mount points" or "extension points".
* These are the places where a plugin can "attach" itself to the application, signaling that it wants to know about certain events and participate in the flow.
* The exact nature of hooks depends heavily on the type of application.
* In our example - hooks allow plugins to intervene in the text-to-HTML transformation.
* The example also demonstrates:
    * 'coarse grained hooks' - processing the whole of the contents
    * 'fine grained hooks' - processing only certain parts of the markup

#### Exposing an Application API to Plugins
* For true flexibility, an application should give plugins access to the application itself.
* In our example - the API is relatively simple. The application simply passes some of its internal objects to the plugins.