# poke-battle

[![Join the chat at https://gitter.im/skooda/poke-battle](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/skooda/poke-battle?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

For now this is a proof of concept project that hopefully is going to become
a tutorial project for writting microservice applications usig
[Nameko](https://github.com/onefinestay/nameko) framework.

Temporary installation note
===========================

 1. Get the source (clone the repo)
 2. 'Install' the development package

 ```
 $ python ./setup.py develop
 ```

 3. Create a temporary db

 ```
 $ python ./make_db.py
 ```

 4. Run services

 ```
 $ nameko run pokebattle.pokemon --config=config.yaml
 $ nameko run pokebattle.players --config=config.yaml
 $ nameko run pokebattle.scores --config=config.yaml
 $ nameko run pokebattle.game_entrypoint --config=config.yaml
```

 Testing
 =======

 ```
$ py.test --cov pokebattle tests/
 ```
