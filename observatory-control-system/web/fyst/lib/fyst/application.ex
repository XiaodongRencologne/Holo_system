defmodule Fyst.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Start the Telemetry supervisor
      FystWeb.Telemetry,
      # Start the PubSub system
      {Phoenix.PubSub, name: Fyst.PubSub},
      # Start the Endpoint (http/https)
      FystWeb.Endpoint,
      # Start a worker by calling: Fyst.Worker.start_link(arg)
      # {Fyst.Worker, arg}
      Fyst.API.child_spec()
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: Fyst.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    FystWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
