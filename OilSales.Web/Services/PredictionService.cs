using System.Net.Http.Json;
using OilSales.Web.Models;

namespace OilSales.Web.Services;

public class PredictionService
{
    private readonly HttpClient _httpClient;

    public PredictionService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<PredictionResponse?> PredictAsync(
        PredictionRequest request)
    {
        var response = await _httpClient.PostAsJsonAsync(
            "predict",
            request
        );

        var responseBody = await response.Content.ReadAsStringAsync();

        if (!response.IsSuccessStatusCode)
        {
            throw new Exception(
                $"Python API Error ({(int)response.StatusCode}): {responseBody}"
            );
        }

        return System.Text.Json.JsonSerializer
            .Deserialize<PredictionResponse>(responseBody);
    }
}