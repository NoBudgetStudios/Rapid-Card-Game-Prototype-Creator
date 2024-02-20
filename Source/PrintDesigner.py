from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from os import listdir
from os.path import isfile, join

def DesignPrint():
    #Gets the pngs
    onlyFiles = [f for f in listdir('.\\..\\Images\\Output\\') if isfile(join('.\\..\\Images\\Output\\', f))]

    png_files = []
    pathPrefix = '.\\..\\Images\\Output\\'
    for file in onlyFiles:
        png_files.append(pathPrefix + file)
    png_files.sort()
    print(len(png_files))

    # Create a new PDF file with A4 page size
    pdf = canvas.Canvas(".\\..\\Images\\PRINT.pdf", pagesize=A4, pageCompression=0)

    # Set the DPI to 300
    dpi = 300
    scale_factor = dpi / 75.6  # Points per inch (72.0)

    # Calculate the width and height in pixels based on DPI
    width_px = int(A4[0] * scale_factor)
    height_px = int(A4[1] * scale_factor)

    # Set the size of the canvas in pixels
    pdf.setPageSize((width_px, height_px))

    # Set the text position
    x = 100 * scale_factor
    y = 500 * scale_factor

    center_x = A4[0]/2
    center_y = A4[1]/2

    mtgCardSize_x = 2.5 * dpi
    mtgCardSize_y = 3.5 * dpi

    space = 50
    imageIndex = 0
    imagesPerPage = 9

    num_pages = (len(png_files) + imagesPerPage - 1) // imagesPerPage  # Ceil division
    
    for pageIndex in range(num_pages):
        #if(imageIndex == len(png_files)): break
        for j in range(-1,2):
            #if(imageIndex == len(png_files)): break
            for i in range(-1,2):
                if(imageIndex == len(png_files)): break
                pdf.drawImage(png_files[imageIndex],
                              (width_px/2 - mtgCardSize_x/2)  + (i * mtgCardSize_x) + i*space,
                              (height_px/2 - mtgCardSize_y/2) + (j * mtgCardSize_y) + j*space)
                print('Total .png files: ' + str(imageIndex))
                imageIndex += 1
        pdf.showPage()
    '''
    for pageIndex in range(num_pages):
        # Calculate the start and end indexes for the images on the current page
        start_index = pageIndex * imagesPerPage
        end_index = min((pageIndex + 1) * imagesPerPage, len(png_files))  # Ensure not to exceed the list length

        for index in range(start_index, end_index):
            i = index % 3  # Calculate i based on the column
            j = index // 3  # Calculate j based on the row

            pdf.drawImage(png_files[index],
                          (width_px / 2 - mtgCardSize_x / 2) + (i * mtgCardSize_x) + i * space,
                          (height_px / 2 - mtgCardSize_y / 2) + (j * mtgCardSize_y) + j * space)
    '''
    pdf.showPage()

    # Save the PDF file
    pdf.save()

    input("\n\nPRESS [ENTER] TO EXIT.")

