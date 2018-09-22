# Guillotina link integrity

The package aims to provide link integrity support for Guillotina.

Features:
- Ability to check for linked content
- Automatically redirect requests when content is renamed or moved
- Manage aliases to content
- Translate resolveuid urls in text


## Dependencies

- Python >= 3.6
- Guillotina
- PG/Cockroachdb


## Installation

This example will use virtualenv:

```
  python -m venv .
  ./bin/pip install .[test]
```


## Running

Running Postgresql Server:

```
docker run --rm -e POSTGRES_DB=guillotina -e POSTGRES_USER=guillotina -p 127.0.0.1:5432:5432 --name postgres postgres:9.6
```


Most simple way to get running:

```
./bin/guillotina
```


# API

The package provides some high level APIs for interacting with content.

Working with linked content:

```python
import guillotina_linkintegrity as li

await li.get_links(ob)
await li.add_links(ob, [ob2, ob3])
await li.remove_links(ob, [ob2, ob3])
await li.update_links_from_html(ob, content)
```

How about aliases:

```python
import guillotina_linkintegrity as li

await li.get_aliases(ob)
await li.add_aliases(ob, ['/foo/bar'])
await li.remove_aliases(ob, ['/foo/bar'])

# what about aliases from parents that might affect it?
await li.get_inherited_aliases(ob)
```

Translate uid linked content:

```python
import guillotina_linkintegrity as li

result = await li.translate_links(content)
```
