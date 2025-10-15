def leap_year(year: int) -> bool:
    # print(year, type(year))
    try:
        year = process_year(year)
        return year%400==0 or (year%4 == 0 and year%100!=0)
    except TypeError:
        return False
    

def process_year(year) -> int:
    """add error handling"""
    if isinstance(year, int):
        return year
    if isinstance(year,str):
        if year.isdigit():
            return int(year)
    raise TypeError
    
    