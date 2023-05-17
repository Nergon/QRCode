from .enums import QRMode, QRErrorCorrectionLevel
from .constants import QR_CODE_VERSIONS
from copy import deepcopy

alphanumeric_characters = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")

def calculate_best_qrmode(data : str):
    """Calculate the best QRMode for the given data. Kanji is not implemented."""
    if data.isdigit():
        return QRMode.NUMERIC
    elif set(data).issubset(alphanumeric_characters):
        return QRMode.ALPHANUMERIC
    else:
        return QRMode.BYTE
    

def calculate_smallest_version(data : str, mode : QRMode,correction : QRErrorCorrectionLevel):
    char_count = len(data)
    for i in range(1,40):
        if char_count <= QR_CODE_VERSIONS[i][QRMode.to_string(mode)][correction.value]:
            return i
    raise ValueError("Data too long for QR Code")


def get_character_count_bits(mode: QRMode, version: int):
    if version <= 9:
        if mode == QRMode.NUMERIC:
            return 10
        elif mode == QRMode.ALPHANUMERIC:
            return 9
        elif mode == QRMode.BYTE:
            return 8
        else:
            raise ValueError("Invalid QRMode")
    elif version <= 26:
        if mode == QRMode.NUMERIC:
            return 12
        elif mode == QRMode.ALPHANUMERIC:
            return 11
        elif mode == QRMode.BYTE:
            return 16
        else:
            raise ValueError("Invalid QRMode")
    else:
        if mode == QRMode.NUMERIC:
            return 14
        elif mode == QRMode.ALPHANUMERIC:
            return 13
        elif mode == QRMode.BYTE:
            return 16
        else:
            raise ValueError("Invalid QRMode")
        

def mask0_func(row, col):
    return (row + col) % 2 == 0

def mask1_func(row, col):
    return row % 2 == 0

def mask2_func(row, col):
    return col % 3 == 0

def mask3_func(row, col):
    return (row + col) % 3 == 0

def mask4_func(row, col):
    return (row // 2 + col // 3) % 2 == 0

def mask5_func(row, col):
    return (row * col) % 2 + (row * col) % 3 == 0

def mask6_func(row, col):
    return ((row * col) % 2 + (row * col) % 3) % 2 == 0

def mask7_func(row, col):
    return ((row * col) % 3 + (row + col) % 2) % 2 == 0

def calc_mask(mask, matrix):
    new_matrix = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            change = False
            if mask == 0:
                change = mask0_func(j,i)
            elif mask == 1:
                change = mask1_func(j,i)
            elif mask == 2:
                change = mask2_func(j,i)
            elif mask == 3:
                change = mask3_func(j,i)
            elif mask == 4:
                change = mask4_func(j,i)
            elif mask == 5:
                change = mask5_func(j,i)
            elif mask == 6:
                change = mask6_func(j,i)
            elif mask == 7:
                change = mask7_func(j,i)

            if change:
                if new_matrix[i][j] == 0:
                    new_matrix[i][j] = 1
                elif new_matrix[i][j] == 1:
                    new_matrix[i][j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if new_matrix[i][j] == -3:
                new_matrix[i][j] = 1
            elif new_matrix[i][j] == -4:
                new_matrix[i][j] = 0
    return new_matrix

def calculate_penalty_score(matrix):
    score = 0
    # First condition: 
    # If there are more than 5 on each color in a row add 3 then 1 for each more
    # Check rows
    for i in range(len(matrix)):
        current_color = matrix[i][0]
        current_count = 1
        for j in range(1,len(matrix[i])):
            if matrix[i][j] == current_color:
                current_count += 1
            else:
                if current_count >= 5:
                    score += 3 + (current_count - 5)
                current_color = matrix[i][j]
                current_count = 1
        if current_count >= 5:
            score += 3 + (current_count - 5)

    # Check columns
    for i in range(len(matrix[0])):
        current_color = matrix[0][i]
        current_count = 1
        for j in range(1,len(matrix)):
            if matrix[j][i] == current_color:
                current_count += 1
            else:
                if current_count >= 5:
                    score += 3 + (current_count - 5)
                current_color = matrix[j][i]
                current_count = 1
        if current_count >= 5:
            score += 3 + (current_count - 5)

    # Second condition:
    # Add 3 to penalty score for each 2x2  block of same color making sure to count overlapping blocks
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                score += 3

    # Third condition:
    # Loom for followining patterns: 00001011101 or 10111010000 and add 40 to penalty score for each horizontal or vertical pattern
    # Check horizontal patterns
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 10):
            if matrix[i][j:j+11] == [0,0,0,0,1,0,1,1,1,0,1] or matrix[i][j:j+11] == [1,0,1,1,1,0,1,0,0,0,0]:
                score += 40
    # Check vertical patterns
    for i in range(len(matrix) - 10):
        for j in range(len(matrix[i])):
            if [matrix[i+k][j] for k in range(11)] == [0,0,0,0,1,0,1,1,1,0,1] or [matrix[i+k][j] for k in range(11)] == [1,0,1,1,1,0,1,0,0,0,0]:
                score += 40

    # Fourth condition:
    # 1. Count the number of total modules in the matrix
    total_modules = len(matrix) * len(matrix[0])
    # 2. Count the number of dark modules
    dark_modules = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                dark_modules += 1
    # 3. Calculate percentage of dark modules (dark modules / total modules)*100
    dark_percentage = (dark_modules / total_modules) * 100
    # 4. Determine previous multiple of five and next multiple of five
    previous_multiple = dark_percentage // 5 * 5
    next_multiple = (dark_percentage // 5 + 1) * 5
    # 5. Subtract 50 from each of this multiples of five and take the absolute value
    previous_difference = abs(previous_multiple - 50)
    next_difference = abs(next_multiple - 50)
    # 6. Divide each of this values by 5
    previous_difference /= 5
    next_difference /= 5
    # 7. Take the lowest value and multiply by 10 and add to penalty score
    score += min(previous_difference,next_difference) * 10
    return score

