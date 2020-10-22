# DNMADe

Site du DNMADe des Herbiers.

## Développement

En utilisant **python 3**:

```
pip install -r requirements.txt
brew install sass/sass/sass
```

Puis 

```
make dev
```

## Déploiement

Le site se déploie tout seul sur GitHub pages grâce à Travis CI à chaque nouveau commit sur la branche `main`.

Pour déployer sur un autre serveur via SCP, il suffit de build le site et de copier les fichiers:
```
make build
scp _build/* <serveur>:<path>
```