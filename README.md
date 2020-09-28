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

```
make build
scp _build/* <serveur>:<path>
```