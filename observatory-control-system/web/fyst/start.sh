#!/bin/sh

export SECRET_KEY_BASE=$(mix phx.gen.secret)

mix compile
mix assets.deploy
mix phx.server

