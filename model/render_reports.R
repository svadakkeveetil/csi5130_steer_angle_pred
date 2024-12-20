render_report = function(submission_filename, img_path, output_filename){
  rmarkdown::render("evaluation_report.Rmd", params = list(
    input_data = submission_filename,
    img_path = img_path
  ),
  output_file = output_filename,
  output_dir = "reports")
}


render_report("submissions/final_model_comma_large_dropout_vp6.csv",
              "phase2_test/center/",
              "final_automatic_report_comma_large_dropout_vp6.html")
