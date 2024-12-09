FROM elixir:1.14

RUN apt-get update && \
    apt-get install -y inotify-tools

RUN mix local.hex --force && \
    mix local.rebar --force

WORKDIR /fyst
COPY ./fyst .

RUN mix setup && \
    mix deps.compile

CMD ["/bin/sh", "start.sh"]
