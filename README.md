# Pseudo Chinese
Convert Japanese to pseudo-Chinese.

## Description
This tool will automatically generate fake Chinese from Japanese sentences.

## Demo
私は本日定時退社します -> 我本日定時退社也

私はお酒を飲みたい -> 我飲酒希望

## Requirement
- Python 3.5.1
- [COTOHA API](https://api.ce-cotoha.com/contents/index.html)

You need to register for a COTOHA API account before you can run this tool.

Once you have registered your COTOHA API account, you will set your Client ID and Client Secret to `env.json` .

```json
{
	"client_id": "yourclinetid",
	"client_secret": "yourclinetsecret"
}
```

## Usage
```
$ python -u pseudo-chinese.py
```

## Contribution
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence

MIT

## Author

[Shoichiro Kono](https://github.com/k2font)
