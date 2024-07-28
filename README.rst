# BaseEmoji

Encode Binary Data Using Emojis! 🙃

![Logo](media/logo.png)

BaseEmoji is a unique binary-to-emoji encoding scheme that converts binary data into a subset of Unicode Emoji symbols. This project, inspired by a desire to make data encoding both fun and distinctive, offers a whimsical alternative to traditional encoding methods like base64.

## Table of Contents
- [Motivation](#motivation)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Release History](#release-history)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Motivation
The primary motivation behind BaseEmoji is to provide a humorous and human-readable way to encode binary data. Traditional methods like base64, while functional, can be mundane. BaseEmoji aims to inject a bit of fun into data encoding and decoding.

## Features
- Basic encode and decode operations.
- [Upcoming] Multiple flavors based on different subsets of Unicode Emoji symbols.
- Opportunities for community contributions.

## Installation
BaseEmoji can be installed via pip:
```sh
pip install base-emoji
```
Alternatively, you can clone the repository directly from GitHub:
```sh
git clone https://github.com/amoallim15/base-emoji.git
```

## Usage
To encode a string into emoji representation:
```sh
$ baseemoji 'Hello world!'
> 😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦
```
To decode the emoji string back to the original text:
```sh
$ baseemoji -d '😀😄😋😪😦😫😫😌😁😛😞😆😄😨😌😈😟😦'
> Hello world!
```

## Release History
- **0.0.3**
  - Added read/write functionality from/to stdin/stdout.
- **0.0.2**
  - Initial implementation with a default emoji subset (base {55}).

## Contributing
I would greatly appreciate it if you could contribute in the form of bug reports, feature suggestions, and pull requests. Please visit our GitHub repository to contribute: [BaseEmoji on GitHub](https://github.com/amoallim15/base-emoji).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please reach out via email at [amoallim15@gmail.com](mailto:amoallim15@gmail.com).
