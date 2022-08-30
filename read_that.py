from pprint import pprint
import tabula as tb


# Notes about area:
# think of the top-left corner as 0,0
# so coordinates of an area would be as follow
# area = (
#   distance_from_top_edge,
#   distance_from_left_edge,
#   bottom_of_table_from_top_edge,
#   widht_of_table_from_left_edge )


box_template = [43, 37, 72, 200]
box_can_am = [171, 46, 814, 560]
box_arctic_cat = [122, 43, 130, 560]

file = "/Users/ekaaditya/Dev/UpworkJobFolder/8x.pdf"

df_header = tb.read_pdf(
    file, pages="all", area=[box_template], stream=True, output_format="json"
)

df_can_am = tb.read_pdf(
    file,
    pages="all",
    area=[box_can_am],
    stream=True,
    output_format="dataframe",
    pandas_options={"header": None},
)

df_arctic_cat = tb.read_pdf(
    file,
    pages="all",
    area=[box_arctic_cat],
    stream=True,
    output_format="dataframe",
    pandas_options={"header": None},
)

header_text = df_header[0]["data"][0][0]["text"]

df_can_am = df_can_am[0]


pprint(header_text)
pprint(df_arctic_cat)
pprint(df_can_am)
