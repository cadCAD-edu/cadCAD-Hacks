INPUT_NOTEBOOK=../cadcad-hack-2-predator-prey-sandbox-model.ipynb
OUTPUT_DIR=output/

# Make sure that we have a clean output/ sub folder
rm -rf $OUTPUT_DIR

# Export to markdown
jupyter nbconvert --to markdown $INPUT_NOTEBOOK --output-dir $OUTPUT_DIR

# Export to PDF through headless browser rendering
jupyter nbconvert --allow-chromium-download --to webpdf $INPUT_NOTEBOOK --output-dir $OUTPUT_DIR

# Export to PDF through LaTeX
jupyter nbconvert --to pdf $INPUT_NOTEBOOK --output-dir $OUTPUT_DIR

# Export to HTML
jupyter nbconvert --to html $INPUT_NOTEBOOK --output-dir $OUTPUT_DIR

# Export to a reveal.js slides deck
jupyter nbconvert --to slides $INPUT_NOTEBOOK --output-dir $OUTPUT_DIR
