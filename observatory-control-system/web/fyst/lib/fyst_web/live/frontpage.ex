defmodule FystWeb.Frontpage do
  use FystWeb, :live_view

  @telescope_interval  2_000
  @weather_interval   60_000

  defp update_telescope(socket) do
    if connected?(socket), do: Process.send_after(self(), :poll_telescope, @telescope_interval)
    {:ok, telescope} = Fyst.API.get_telescope_status()
    assign(socket, :telescope, telescope)
  end

  defp update_weather(socket) do
    if connected?(socket), do: Process.send_after(self(), :poll_weather, @weather_interval)
    {:ok, weather} = Fyst.API.get_weather()
    assign(socket, :weather, weather)
  end

  def mount(_params, _session, socket) do
    {:ok, socket |> update_telescope |> update_weather }
  end

  def handle_info(:poll_telescope, socket) do
    {:noreply, update_telescope(socket)}
  end

  def handle_info(:poll_weather, socket) do
    {:noreply, update_weather(socket)}
  end
end
