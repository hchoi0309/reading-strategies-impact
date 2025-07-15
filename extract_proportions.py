import fitz
import pytesseract
import cv2
import numpy as np
import pandas as pd
from PIL import Image

def extract_proportions(folder_path, num_pdfs):
    '''
    Extract the proportion of highlighted text from pdf files titled with numbers in the folder_path
    '''
    # Initialize a dictionary to store the proportions
    # The key will be the pdf id and the value will be the proportion of highlighted text
    proportions = {}

    # Iterate through the pdfs in the folder
    for id in range(1, num_pdfs + 1):
        try:
            # Open the pdf
            pdf_path = f"{folder_path}/{id}.pdf"
            doc = fitz.open(pdf_path)

            total_text = ""
            highlighted_text = ""

            # Process each page
            for page in doc:
                # Convert the page to an image
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better resolution (double the number of pixels)
                # Convert the image from RGBA (pixmap default format) to RGB
                img = Image.frombytes(mode="RGB", size=[pix.width, pix.height], data=pix.samples) # check later if refactoring is possible
                img_np = np.array(img)

                # Detect highlighted areas in yellow
                # Convert the image to HSV colour space
                hsv = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)
                # Define the range for the yellow colour in HSV
                lower_yellow = np.array([20, 100, 100])
                upper_yellow = np.array([35, 255, 255])
                # Create a mask for yellow areas
                mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

                # Clean up mask
                kernel = np.ones((3,3), np.uint8)
                mask = cv2.dilate(mask, kernel, iterations=1)

                # Get total text
                total_text += pytesseract.image_to_string(img_np)

                # Get highlighted text
                highlighted = cv2.bitwise_and(img_np, img_np, mask=mask)
                highlighted_text += pytesseract.image_to_string(highlighted)

            doc.close()

            # Calculate proportion of highlighted text
            total_length = len(total_text.strip())
            highlighted_length = len(highlighted_text.strip())
            proportion = (highlighted_length / total_length * 100) if total_length > 0 else 0
            proportions[id] = proportion

            print("Total text length:", total_length)
            print("Highlighted text length:", highlighted_length)
        
        except Exception as e:
            print(f"Error while processing the {id}th pdf: {e}")

    return proportions

def update_proportions(output_path, output_sheet, proportions):
    '''
    Update the csv file located at output_path by adding a column of proportions
    '''
    try:
        # Read existing csv from output_path
        df = pd.read_excel(output_path, sheet_name=output_sheet)
        # Add the proportions to the dataframe based on matching id values
        df["highlight_proportion"] = df["id"].map(proportions)
        # Save the updated csv file to the same path
        df.to_excel(output_path, sheet_name=output_sheet, index=False)

    except Exception as e:
        print("Error while updating the excel file:", e)

def main():
    folder_path = "data/passages/highlighted_passages"
    num_pdfs = 2
    proportions = extract_proportions(folder_path, num_pdfs)
    print("\n\n{}".format(proportions))

    output_path, output_sheet = "data/participant_responses.xls", "highlighted_portions"
    update_proportions(output_path, output_sheet, proportions)
    # print("Successful Completion")

if __name__ == "__main__":
    main()
