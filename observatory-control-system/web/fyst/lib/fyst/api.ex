defmodule Fyst.API do

  def child_spec() do
    {Finch, name: __MODULE__}
  end

  defp get(path) do
    url = URI.merge("http://api:8000/", path)
    response = Finch.build(:get, url) |> Finch.request(__MODULE__)
    case response do
      {:ok, %Finch.Response{body: body}} -> {:ok, Jason.decode!(body)}
      _ -> response
    end
  end

  def get_weather() do
    get("/weather/current")
  end

  def get_telescope_status() do
    get("/telescope/status")
  end

end
