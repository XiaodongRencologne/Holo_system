import Config

# We don't run a server during test. If one is required,
# you can enable the server option below.
config :fyst, FystWeb.Endpoint,
  http: [ip: {127, 0, 0, 1}, port: 4002],
  secret_key_base: "V2g7GwQhp2VCKcmAnn4huW1BDrIiIzLmeycmq3j/n2FOpcreZOivQD4F1Qq9UKg1",
  server: false

# Print only warnings and errors during test
config :logger, level: :warning

# Initialize plugs at runtime for faster test compilation
config :phoenix, :plug_init_mode, :runtime
