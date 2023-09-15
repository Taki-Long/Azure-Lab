## Setup

1. Install Node 18 https://nodejs.org/en
2. Install Python 3.10
3. Install NPM Tools
```shell
npm install -g yarn
npm install -g @azure/static-web-apps-cli
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```


## Develop
Run in repo root.
```shell
swa start
```

## Deploy

```shell
swa build
swa deploy --deployment-token {token from static web app}
```

