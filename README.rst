BaseEmoji 
=========

	Encode everything in Emojis! 🙃

.. image:: media/logo.png

BaseEmoji is a binary-to-emoji encoding scheme that represent binary data in a subset of the Unicode Emoji symbols, designed for triggering senior programmers effortlessly.
BaseEmoji is heavily influenced by my furstration towards my tech lead that always shares data (base64 encoded) with me.

But why?
--------

- MOCKERY!
- WHY NOT!
- Base64 is not the best scheme to represent and transmit (mostly binary) data in a human-readable way. ¯\_(ツ)_/¯

Features
--------

- Basic encode/decode operations.
- Different encoding schemes based on Uincode Emoji groups.
- [Contribute].

Installation
------------
You can install the package by issuing the following command:

::
	
	pip install base-emoji


You can also clone this project using git:

::
	
	git clone https://github.com/amoallim15/base-emoji.git

Usage example
-------------

Basic usage looks like:

::

	$ baseemoji 'Hello world!'
	> 😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦
	$ baseemoji -d '😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦'
	> Hello world!

Release History
---------------

* 0.0.1
    * Initial implementation with a default flavor of base {55}.

About
-----

Ali Moallim – amoallim15@gmail.com

Contributing
------------

Bug reports and pull requests are welcome on GitHub at https://github.com/amoallim15/base-emoji.
I'm also available for questions, feel free to get in touch.

License
-------

The package is available as open source under the terms of the `MIT License`_.

.. _MIT License: http://www.python.org/
