def leap_year(year: int) -> bool:
    # print(year, type(year))
    try:
        year = process_year(year)
    except TypeError:
        return False
    return year%400==0 or (year%4 == 0 and year%100!=0)

def process_year(year) -> int:
    if isinstance(year, int):
        return year
    if isinstance(year,str):
        if year.isdigit():
            return int(year)
    raise TypeError
    
    