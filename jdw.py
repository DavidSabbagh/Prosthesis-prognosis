import pandas as pd

xls = pd.ExcelFile('./Stats_David.xlsx')

# clinical outcomes to predict...
y = pd.read_excel(xls, 'COMPL+Clinic FU', header=2).set_index('No.')
yAFE = y['A FE °']  # forward elevation in degree, the higher the better
yAIR = y['A IR (Hand)']  # highest vertebra touched,
# buttock < SI (< L5 < L4) < L3 (< L2 < L1) < T12 < T8
yAER = y['A ER°']  # external rotation in degree, the higher the better
yPAIN = y['Pain ']  # felt pain, the higher the worst
yCST = y['Total']  # fonctional score, the higher the better
y = yAFE

# ...from prosthesis position
preX = pd.read_excel(xls, 'Preop Rx', header=0)
preX = preX[['No.', 'CSA', 'LSA', 'DSA', 'Glene - CDR', 'Glene-GT',
             'H: Acromion-GT', 'L: Acromion - GT', 'Beta Angle',
             'Tilt Horizontale', 'Tilt fosse/Horizontale']]
preX.columns = ['No.', 'CSA', 'preLSA', 'preDSA', 'preGleneCDR', 'preGleneGT',
                'preAcriomonH', 'preAcromionL', 'preBetaAngle',
                'preTiltH', 'preTiltF']

postX = pd.read_excel(xls, 'Postop RX', header=0)
postX = postX[['No.', 'LSA', 'DSA', 'CDR-Glenoid', 'GT-Glenoid',
               'H: Acromion-GT', 'L: Acromion - GT', 'Beta Angle',
               'Tilt Verticale', 'Tilt fosse/Horizontale']]
postX.columns = ['No.', 'postLSA', 'postDSA', 'postGleneCDR', 'postGleneGT',
                 'postAcriomonH', 'postAcromionL', 'postBetaAngle',
                 'postTiltH', 'postTiltF']

X = pd.merge(preX, postX, on='No.')
X = X.set_index('No.')
