using System.Text.Json.Serialization;

namespace OilSales.Web.Models;

public class PredictionRequest
{
    [JsonPropertyName("average_price")]
    public double AveragePrice { get; set; }

    [JsonPropertyName("volume_sales")]
    public double VolumeSales { get; set; }

    [JsonPropertyName("year")]
    public int Year { get; set; }

    [JsonPropertyName("month")]
    public int Month { get; set; }

    [JsonPropertyName("city")]
    public string City { get; set; } = string.Empty;

    [JsonPropertyName("manufacturer")]
    public string Manufacturer { get; set; } = string.Empty;

    [JsonPropertyName("brand")]
    public string Brand { get; set; } = string.Empty;

    [JsonPropertyName("product_class")]
    public string ProductClass { get; set; } = string.Empty;

    [JsonPropertyName("price_bracket")]
    public string PriceBracket { get; set; } = string.Empty;
}