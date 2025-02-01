import cv2

# Load the image
image_path = '\\assessets\\soccer_practice.jpg'
ip_img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Check if image is loaded
if ip_img is None:
    print("Error: Image not found. Check the file path!")
else:
    # Rotate the image in different directions
    rotations = [
        (cv2.ROTATE_90_CLOCKWISE, "90 degrees"),
        (cv2.ROTATE_180, "180 degrees"),
        (cv2.ROTATE_90_COUNTERCLOCKWISE, "270 degrees"),  # 270 degrees is counter-clockwise
        "Original (360 degrees)"  # 360 degrees is the same as the original image
    ]
    
    # Apply each rotation and display it
    for rotation, label in rotations:
        if label == "Original (360 degrees)":
            rotated_image = ip_img  # Original image
        else:
            rotated_image = cv2.rotate(ip_img, rotation)
        
        # Show the rotated image
        cv2.imshow(f'Rotated Image - {label}', rotated_image)
        cv2.waitKey(0)

        # Save the rotated image
        output_path = f'C:\\Users\\Dr. HOMEIRA NISHAT\\Desktop\\see\\output_{label.replace(" ", "_")}.jpg'
        cv2.imwrite(output_path, rotated_image)
        print(f"Image saved at: {output_path}")
    
    cv2.destroyAllWindows()
