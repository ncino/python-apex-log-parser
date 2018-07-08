# python-apex-log-parser
A quick tool for working with Salesforce Subscriber logs.

This was created for my own benefit when examining Salesforce logs to locate efficiency problems like repeated SQOL Queries, non-double fire safe triggers and things like that. If it proves useful, I will continue updating it and am happy to review enhancements/corrections.

With that said, it is very immature - so use at your own risk!

## Getting Started

The only prerequisite is that you have some recent version of Python installed.

To use, simply clone the repo, navigate to the root folder and execute the following command:

```
python main.py [path to subscriber log] [destination path for json file]
```

## Authors

* **Royce Nobles** - *Initial work* - (https://github.com/roycenobles)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details