BaseEmoji
==========

Encode Binary Data Using Emojis! 🙃

.. image:: media/logo.png

BaseEmoji is a unique binary-to-emoji encoding scheme that converts binary data into a subset of Unicode Emoji symbols. This project, inspired by a desire to make data encoding both fun and distinctive, offers a whimsical alternative to traditional encoding methods like base64.

Table of Contents
=================
- `Motivation <#motivation>`_
- `Features <#features>`_
- `Installation <#installation>`_
- `Usage <#usage>`_
- `Release History <#release-history>`_
- `Contributing <#contributing>`_
- `License <#license>`_
- `Contact <#contact>`_

Motivation
==========
The primary motivation behind BaseEmoji is to provide a humorous and human-readable way to encode binary data. Traditional methods like base64, while functional, can be mundane. BaseEmoji aims to inject a bit of fun into data encoding and decoding.

Features
========
- Basic encode and decode operations.
- [Upcoming] Multiple flavors based on different subsets of Unicode Emoji symbols.
- Opportunities for community contributions.

Installation
============
BaseEmoji can be installed via pip::

    pip install base-emoji

Alternatively, you can clone the repository directly from GitHub::

    git clone https://github.com/amoallim15/base-emoji.git

Usage
=====
To encode a string into emoji representation::

    $ baseemoji 'Hello world!'
    > 😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦

To decode the emoji string back to the original text::

    $ baseemoji -d '😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦'
    > Hello world!

Release History
===============
- **0.0.3**
  - Added read/write functionality from/to stdin/stdout.
- **0.0.2**
  - Initial implementation with a default emoji subset (base {55}).

Contributing
============
Contributions in the form of bug reports, feature suggestions, and pull requests are highly appreciated. Please visit our GitHub repository to contribute: `BaseEmoji on GitHub <https://github.com/amoallim15/base-emoji>`_.

License
=======
This project is licensed under the MIT License. See the `LICENSE <LICENSE>`_ file for details.

Contact
=======
For any inquiries, please reach out via email at `amoallim15@gmail.com <mailto:amoallim15@gmail.com>`_.
