"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

LINES = ['5x5:1401000100010140504200010',
         '8x6:101014003023000400010051401301005000000800121000',
         '9x7:004000001147000150000610010016000000030121080000020013010860001',
         '11x8:4100140010002100000031000161700500130440001203100401051100601000084100100001000010413100',
         '10x10:0001056010666000000400044000300000041033107551400100000001033100810001100106505006100700021001000001',
         '13x9:314010001001000019000890060100001000060100100010010003064410070403004000000010505160616060030031440500010010004000130',
         '10x15:100010000001410301886000071000010500309000010103000100000101401045001216044001000100010008005100010001000126100010080005008610010001600030400000131040',
         '17x13:10100100000005001006410100160050101000033084151600280180001400050661000300000010500000031661010010073300106000760004190040010613304033000030001001000000140190000050101000050801017040000010500031000000500001001001061310140',
         '16x18:710010051401000000502050010005800101010000330100001000008063170001514123600000071000001030100100010100410001043103001007000090001090000008121210300050010100010501010055000000400003100130105440100043101300070605041006007770900400501441000000331001000010001010001500100014020000090107004010',
         '20x20:0170014131400140101403000000030160040200010100101010021000000400030000003200151001613001007100040130001009100100010000510080060140100020010000001600610190401002010000001000010006021000780005661001031031001015010005131400001061001777700030011060000100000000051400407317000849003100101810300133040133100500001000304107005010100000100810003100210661055000055202100400004001707002000610014001000010100001',
         '20x25:16010100000100010171410050500100810020000400100610100891001007007901600010003103001000001001056300010160180000000000021605005170700101001040010000100010301000400544150330030053100000440010100001000073000100310810101000100133080301010058100007010010040010100701000000301901330001001004034230000100103001081000010010000014205005050016009801075057005570000680000000100100003300101001000100008130010004400010662100044831481010960020070000100000010001000910000007160300501001010440100008010000000341000610',
         ]


def line2grid(line):
    """ Reshape the line into a grid, thanks to the given dim. """
    dim, line = line.split(':')
    nb_cols, nb_rows = map(int, dim.split('x'))
    rows = (line[i * nb_cols: (i + 1) * nb_cols] for i in range(nb_rows))
    return nb_cols * nb_rows, [list(map(int, row)) for row in rows]


TESTS = {'Basics': [], 'Extra': []}

for nb_boxes, grid in map(line2grid, LINES):
    category = ('Basics', 'Extra')[nb_boxes > 50]
    TESTS[category].append({'input': grid, 'answer': grid})

# # ----- for initial code ----- #
# GRIDS = (d['input'] for d in TESTS['Basics'])
# GRIDS = tuple((f'{len(grid)}x{len(grid[0])}', grid) for grid in GRIDS)
# print('GRIDS =', GRIDS)
