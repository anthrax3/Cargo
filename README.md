## Cargo ##
Welcome to Cargo! Cargo is a framework for loading and executing modules written in Python focused on Computer and Network Security. It acts as a front-end for penetration testing, exploitation, reverse-engineering and information gathering tools. Using *attributes* that Cargo can set and expose to it's *modules* the user can control the behaviour of the modules, as well as execute them and monitor their actions.

## Yes but what does it do? ##
Cargo is currently in heavy development. Features currently implemented are *module* loading and executing, *attribute* setting, and of course command parsing. More features are to be added in the next update.

## How do I...? ##
Loading *modules* is really easy, just type ### load *cargo-path-to-module ###. The Cargo path root is cargo and you can load any module that is contained in that directory by specifying it's full path, separating directories by dots. (Example: use cargo.modules.exploits.template)

Setting *attributes* is even easier. Just type ### set *attribute-name* *value* ###. Make sure you have loaded a module before that, though!

Unloading a *module* can be done by typing ### unload ###.

Running a module is as simple as ### run ###.

Exit Cargo by typing ### exit ###.

## So what *modules* are available? ##
As of yet, no *modules* are avalailable on this repo, but many are under heavy developement and will be released soon. For testing and developement purposes, there is a *module* under the Cargo path *cargo.modules.exploits.template* that can be loaded and executed.
