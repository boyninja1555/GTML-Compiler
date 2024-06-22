import argparse
import os
from gtml_parser import gtml_parser

def main():
    parser = argparse.ArgumentParser(description="Compile GTML to HTML")
    parser.add_argument("filepath", type=str, help="Path to the GTML file")
    args = parser.parse_args()

    # Read the specified GTML file
    with open(args.filepath, "r") as file:
        gtml_content = file.read()

    # Parse the contents of the GTML file
    new_gtml_parser = gtml_parser(gtml_content)
    new_gtml_parser.parse()
    html_output = new_gtml_parser.compile_to_html()

    # Construct output path
    gtml_dir = os.path.dirname(args.filepath)
    bin_dir = os.path.join(gtml_dir, "bin")
    os.makedirs(bin_dir, exist_ok=True)

    # Write the output HTML file to the bin folder
    output_filename = os.path.splitext(os.path.basename(args.filepath))[0] + ".html"
    output_filepath = os.path.join(bin_dir, output_filename)

    with open(output_filepath, "w") as output_file:
        output_file.write(html_output)

    # Let user know that the process has finished
    print(f"HTML output compiled to {output_filepath}")

    # Ask user if they want to open the HTML file in their browser
    open_in_browser = input("Would you like to open the HTML file in your browser? (y/n) ")
    if open_in_browser.lower() == "y":
        import webbrowser
        webbrowser.open(output_filepath, new=2)
    else:
        print("Ok.")

if __name__ == "__main__":
    main()
