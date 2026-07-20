using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using OilSales.Web.Models;
using OilSales.Web.Services;

namespace OilSales.Web.Pages.Prediction;

public class IndexModel : PageModel
{
    private readonly PredictionService _predictionService;

    public IndexModel(
        PredictionService predictionService)
    {
        _predictionService = predictionService;
    }


    [BindProperty]
    public PredictionRequest Prediction { get; set; }
        = new();


    public double? PredictedValueSales { get; set; }


    public string? ErrorMessage { get; set; }


    public void OnGet()
    {
        Prediction.Year = DateTime.Now.Year;

        Prediction.Month = DateTime.Now.Month;
    }


    public async Task<IActionResult> OnPostAsync()
    {
        if (!ModelState.IsValid)
        {
            return Page();
        }


        try
        {
            var result =
                await _predictionService
                    .PredictAsync(Prediction);


            PredictedValueSales =
                result?.PredictedValueSales;


            return Page();
        }
        catch (Exception ex)
        {
            ErrorMessage = ex.Message;

            return Page();
        }
    }
}