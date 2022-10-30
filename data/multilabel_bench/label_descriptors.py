ICD9_CONCEPTS = {
    "level_1": {
        "001-139": ("Infection and Parasitic Diseases", "Infections"),
        "140-239": ("Neoplasms", "Neoplasms"),
        "240-279": ("Endocrine, Nutritional and Metabolic Diseases and Immunity Disorders", "Metabolic"),
        "280-289": ("Diseases of Blood and Blood Forming Organs", "Blood"),
        "290-319": ("Mental Disorders", "Mental"),
        "320-389": ("Diseases of Nervous System and Sense Organs", "Nervous"),
        "390-459": ("Diseases of the Circulatory System", "Circulatory"),
        "460-519": ("Diseases of the Respiratory System", "Respiratory"),
        "520-579": ("Diseases of the Digestive System", "Digestive"),
        "580-629": ("Diseases of the Genitourinary System", "Genitourinary"),
        "630-676": ("Complications of Pregnancy, Childbirth and the Puerperium", "Pregnancy"),
        "680-709": ("Diseases of the Skin and Subcutaneous Tissue", "Skin"),
        "710-739": ("Diseases of the Musculoskeletal System and Connective Tissue", "Musculoskeletal"),
        "740-759": ("Congenital Anomalies", "Anomalies"),
        "760-779": ("Certain Conditions Originating in the Perinatal Period", "Perinatal"),
        "780-799": ("Symptoms, Signs and Ill-defined Conditions", "Symptoms"),
        "800-999 ": ("Injury and Poisoning", "Injury"),
        "V01-V91": ("Supplementary Factors Influencing Health Status and Contact with Health Services", "Services"),
        "E000-E999": ("Supplementary Classification Of External Causes Of Injury And Poisoning", "External"),
    },
    "level_2": {'001-009': 'Intestinal Infectious Diseases', '010-018': 'Tuberculosis',
                '020-027': 'Zoonotic Bacterial Diseases', '030-041': 'Other Bacterial Diseases',
                '042-042': 'Human Immunodeficiency Virus',
                '045-049': 'Poliomyelitis And Other Non-Arthropod-Borne Viral Diseases Of Central Nervous System',
                '050-059': 'Viral Diseases Accompanied By Exanthem', '060-066': 'Arthropod-Borne Viral Diseases',
                '070-079': 'Other Diseases Due To Viruses And Chlamydiae',
                '080-088': 'Rickettsioses And Other Arthropod-Borne Diseases',
                '090-099': 'Syphilis And Other Venereal Diseases', '100-104': 'Other Spirochetal Diseases',
                '110-118': 'Mycoses', '120-129': 'Helminthiases',
                '130-136': 'Other Infectious And Parasitic Diseases',
                '137-139': 'Late Effects Of Infectious And Parasitic Diseases',
                '140-149': 'Malignant Neoplasm Of Lip, Oral Cavity, And Pharynx',
                '150-159': 'Malignant Neoplasm Of Digestive Organs And Peritoneum',
                '160-165': 'Malignant Neoplasm Of Respiratory And Intrathoracic Organs',
                '170-176': 'Malignant Neoplasm Of Bone, Connective Tissue, Skin, And Breast',
                '179-189': 'Malignant Neoplasm Of Genitourinary Organs',
                '190-199': 'Malignant Neoplasm Of Other And Unspecified Sites',
                '200-209': 'Malignant Neoplasm Of Lymphatic And Hematopoietic Tissue', '210-229': 'Benign Neoplasms',
                '230-234': 'Carcinoma In Situ', '235-238': 'Neoplasms Of Uncertain Behavior',
                '239-239': 'Neoplasms Of Unspecified Nature', '240-246': 'Disorders Of Thyroid Gland',
                '249-259': 'Diseases Of Other Endocrine Glands', '260-269': 'Nutritional Deficiencies',
                '270-279': 'Other Metabolic Disorders And Immunity Disorders', '280': 'Iron deficiency anemias',
                '281': 'Other deficiency anemias', '282': 'Hereditary hemolytic anemias',
                '283': 'Acquired hemolytic anemias', '284': 'Aplastic anemia and other bone marrow failure syndromes',
                '285': 'Other and unspecified anemias', '286': 'Coagulation defects',
                '287': 'Purpura and other hemorrhagic conditions', '288': 'Diseases of white blood cells',
                '289': 'Other diseases of blood and blood-forming organs', '290-294': 'Organic Psychotic Conditions',
                '295-299': 'Other Psychoses',
                '300-316': 'Neurotic Disorders, Personality Disorders, And Other Nonpsychotic Mental Disorders',
                '317-319': 'Intellectual Disabilities',
                '320-327': 'Inflammatory Diseases Of The Central Nervous System',
                '330-337': 'Hereditary And Degenerative Diseases Of The Central Nervous System', '338-338': 'Pain',
                '339-339': 'Other Headache Syndromes', '340-349': 'Other Disorders Of The Central Nervous System',
                '350-359': 'Disorders Of The Peripheral Nervous System', '360-379': 'Disorders Of The Eye And Adnexa',
                '380-389': 'Diseases Of The Ear And Mastoid Process', '390-392': 'Acute Rheumatic Fever',
                '393-398': 'Chronic Rheumatic Heart Disease', '401-405': 'Hypertensive Disease',
                '410-414': 'Ischemic Heart Disease', '415-417': 'Diseases Of Pulmonary Circulation',
                '420-429': 'Other Forms Of Heart Disease', '430-438': 'Cerebrovascular Disease',
                '440-449': 'Diseases Of Arteries, Arterioles, And Capillaries',
                '451-459': 'Diseases Of Veins And Lymphatics, And Other Diseases Of Circulatory System',
                '460-466': 'Acute Respiratory Infections', '470-478': 'Other Diseases Of Upper Respiratory Tract',
                '480-488': 'Pneumonia And Influenza',
                '490-496': 'Chronic Obstructive Pulmonary Disease And Allied Conditions',
                '500-508': 'Pneumoconioses And Other Lung Diseases Due To External Agents',
                '510-519': 'Other Diseases Of Respiratory System',
                '520-529': 'Diseases Of Oral Cavity, Salivary Glands, And Jaws',
                '530-539': 'Diseases Of Esophagus, Stomach, And Duodenum', '540-543': 'Appendicitis',
                '550-553': 'Hernia Of Abdominal Cavity', '555-558': 'Noninfective Enteritis And Colitis',
                '560-569': 'Other Diseases Of Intestines And Peritoneum',
                '570-579': 'Other Diseases Of Digestive System',
                '580-589': 'Nephritis, Nephrotic Syndrome, And Nephrosis',
                '590-599': 'Other Diseases Of Urinary System', '600-608': 'Diseases Of Male Genital Organs',
                '610-612': 'Disorders Of Breast', '614-616': 'Inflammatory Disease Of Female Pelvic Organs',
                '617-629': 'Other Disorders Of Female Genital Tract',
                '630-639': 'Ectopic And Molar Pregnancy And Other Pregnancy With Abortive Outcome',
                '640-649': 'Complications Mainly Related To Pregnancy',
                '650-659': 'Normal Delivery, And Other Indications For Care In Pregnancy, Labor, And Delivery',
                '660-669': 'Complications Occurring Mainly In The Course Of Labor And Delivery',
                '670-677': 'Complications Of The Puerperium', '678-679': 'Other Maternal And Fetal Complications',
                '680-686': 'Infections Of Skin And Subcutaneous Tissue',
                '690-698': 'Other Inflammatory Conditions Of Skin And Subcutaneous Tissue',
                '700-709': 'Other Diseases Of Skin And Subcutaneous Tissue',
                '710-719': 'Arthropathies And Related Disorders', '720-724': 'Dorsopathies',
                '725-729': 'Rheumatism, Excluding The Back',
                '730-739': 'Osteopathies, Chondropathies, And Acquired Musculoskeletal Deformities',
                '740': 'Anencephalus and similar anomalies', '741': 'Spina bifida',
                '742': 'Other congenital anomalies of nervous system', '743': 'Congenital anomalies of eye',
                '744': 'Congenital anomalies of ear face and neck',
                '745': 'Bulbus cordis anomalies and anomalies of cardiac septal closure',
                '746': 'Other congenital anomalies of heart', '747': 'Other congenital anomalies of circulatory system',
                '748': 'Congenital anomalies of respiratory system', '749': 'Cleft palate and cleft lip',
                '750': 'Other congenital anomalies of upper alimentary tract',
                '751': 'Other congenital anomalies of digestive system',
                '752': 'Congenital anomalies of genital organs', '753': 'Congenital anomalies of urinary system',
                '754': 'Certain congenital musculoskeletal deformities', '755': 'Other congenital anomalies of limbs',
                '756': 'Other congenital musculoskeletal anomalies', '757': 'Congenital anomalies of the integument',
                '758': 'Chromosomal anomalies', '759': 'Other and unspecified congenital anomalies',
                '760-763': 'Maternal Causes Of Perinatal Morbidity And Mortality',
                '764-779': 'Other Conditions Originating In The Perinatal Period', '780-789': 'Symptoms',
                '790-796': 'Nonspecific Abnormal Findings',
                '797-799': 'Ill-Defined And Unknown Causes Of Morbidity And Mortality',
                '800-804': 'Fracture Of Skull', '805-809': 'Fracture Of Spine And Trunk',
                '810-819': 'Fracture Of Upper Limb', '820-829': 'Fracture Of Lower Limb', '830-839': 'Dislocation',
                '840-848': 'Sprains And Strains Of Joints And Adjacent Muscles',
                '850-854': 'Intracranial Injury, Excluding Those With Skull Fracture',
                '860-869': 'Internal Injury Of Chest, Abdomen, And Pelvis',
                '870-879': 'Open Wound Of Head, Neck, And Trunk', '880-887': 'Open Wound Of Upper Limb',
                '890-897': 'Open Wound Of Lower Limb', '900-904': 'Injury To Blood Vessels',
                '905-909': 'Late Effects Of Injuries, Poisonings, Toxic Effects, And Other External Causes',
                '910-919': 'Superficial Injury', '920-924': 'Contusion With Intact Skin Surface',
                '925-929': 'Crushing Injury', '930-939': 'Effects Of Foreign Body Entering Through Orifice',
                '940-949': 'Burns', '950-957': 'Injury To Nerves And Spinal Cord',
                '958-959': 'Certain Traumatic Complications And Unspecified Injuries',
                '960-979': 'Poisoning By Drugs, Medicinals And Biological Substances',
                '980-989': 'Toxic Effects Of Substances Chiefly Nonmedicinal As To Source',
                '990-995': 'Other And Unspecified Effects Of External Causes',
                '996-999': 'Complications Of Surgical And Medical Care, Not Elsewhere Classified',
                'E000-E000': 'External Cause Status', 'E001-E030': 'Activity', 'E800-E807': 'Railway Accidents',
                'E810-E819': 'Motor Vehicle Traffic Accidents', 'E820-E825': 'Motor Vehicle Nontraffic Accidents',
                'E826-E829': 'Other Road Vehicle Accidents', 'E830-E838': 'Water Transport Accidents',
                'E840-E845': 'Air And Space Transport Accidents',
                'E846-E849': 'Vehicle Accidents, Not Elsewhere Classifiable',
                'E850-E858': 'Accidental Poisoning By Drugs, Medicinal Substances, And Biologicals',
                'E860-E869': 'Accidental Poisoning By Other Solid And Liquid Substances, Gases, And Vapors',
                'E870-E876': 'Misadventures To Patients During Surgical And Medical Care',
                'E878-E879': 'Surgical And Medical Procedures As The Cause Of Abnormal Reaction Of Patient Or Later Complication, Without Mention Of Misadventure At The Time Of Procedure',
                'E880-E888': 'Accidental Falls', 'E890-E899': 'Accidents Caused By Fire And Flames',
                'E900-E909': 'Accidents Due To Natural And Environmental Factors',
                'E910-E915': 'Accidents Caused By Submersion, Suffocation, And Foreign Bodies',
                'E916-E928': 'Other Accidents', 'E929-E929': 'Late Effects Of Accidental Injury',
                'E930-E949': 'Drugs, Medicinal And Biological Substances Causing Adverse Effects In Therapeutic Use',
                'E950-E959': 'Suicide And Self-Inflicted Injury',
                'E960-E969': 'Homicide And Injury Purposely Inflicted By Other Persons',
                'E970-E979': 'Legal Intervention',
                'E980-E989': 'Injury Undetermined Whether Accidentally Or Purposely Inflicted',
                'E990-E999': 'Injury Resulting From Operations Of War',
                'V01-V09': 'Persons With Potential Health Hazards Related To Communicable Diseases',
                'V10-V19': 'Persons With Potential Health Hazards Related To Personal And Family History',
                'V20-V29': 'Persons Encountering Health Services In Circumstances Related To Reproduction And Development',
                'V30-V39': 'Liveborn Infants According To Type Of Birth',
                'V40-V49': 'Persons With A Condition Influencing Their Health Status',
                'V50-V59': 'Persons Encountering Health Services For Specific Procedures And Aftercare',
                'V60-V69': 'Persons Encountering Health Services In Other Circumstances',
                'V70-V82': 'Persons Without Reported Diagnosis Encountered During Examination And Investigation Of Individuals And Populations',
                'V83-V84': 'Genetics', 'V85-V85': 'Body Mass Index', 'V86-V86': 'Estrogen Receptor Status',
                'V87-V87': 'Other Specified Personal Exposures And History Presenting Hazards To Health',
                'V88-V88': 'Acquired Absence Of Other Organs And Tissue',
                'V89-V89': 'Other Suspected Conditions Not Found', 'V90-V90': 'Retained Foreign Body',
                'V91-V91': 'Multiple Gestation Placenta Status'}

}

EUROVOC_CONCEPTS = {
    'level_1': {'100142': ('politics', 'politics'),
                '100143': ('international relations', 'international'),
                '100144': ('european union', 'european'),
                '100145': ('law', 'law'),
                '100146': ('economics', 'economics'),
                '100147': ('trade', 'trade'),
                '100148': ('finance', 'finance'),
                '100149': ('social questions', 'social'),
                '100150': ('education and communications', 'education'),
                '100151': ('science', 'science'),
                '100152': ('business and competition', 'business'),
                '100153': ('employment and working conditions', 'employment'),
                '100154': ('transport', 'transport'),
                '100155': ('environment', 'environment'),
                '100156': ('agriculture, forestry and fisheries', 'agriculture'),
                '100157': ('agri-foodstuffs', 'food'),
                '100158': ('production, technology and research', 'production'),
                '100159': ('energy', 'energy'),
                '100160': ('industry', 'industry'),
                '100161': ('geography', 'geography'),
                '100162': ('international organisations', 'organisations'),
                },
    'level_2': {'100163': 'political framework', '100164': 'political party',
                '100165': 'electoral procedure and voting', '100166': 'parliament',
                '100167': 'parliamentary proceedings', '100168': 'politics and public safety',
                '100169': 'executive power and public service', '100170': 'international affairs',
                '100171': 'cooperation policy', '100172': 'international security', '100173': 'defence',
                '100174': 'EU institutions and European civil service', '100175': 'European Union law',
                '100176': 'European construction', '100177': 'EU finance', '100178': 'sources and branches of the law',
                '100179': 'civil law', '100180': 'criminal law', '100181': 'justice',
                '100182': 'organisation of the legal system', '100183': 'international law',
                '100184': 'rights and freedoms', '100185': 'economic policy', '100186': 'economic conditions',
                '100187': 'regions and regional policy', '100188': 'economic structure', '100189': 'national accounts',
                '100190': 'economic analysis', '100191': 'trade policy', '100192': 'tariff policy', '100193': 'trade',
                '100194': 'international trade', '100195': 'consumption', '100196': 'marketing',
                '100197': 'distributive trades', '100198': 'monetary relations', '100199': 'monetary economics',
                '100200': 'financial institutions and credit', '100201': 'free movement of capital',
                '100202': 'financing and investment', '100203': 'insurance',
                '100204': 'public finance and budget policy', '100205': 'budget', '100206': 'taxation',
                '100207': 'prices', '100208': 'family', '100209': 'migration', '100210': 'demography and population',
                '100211': 'social framework', '100212': 'social affairs', '100213': 'culture and religion',
                '100214': 'social protection', '100215': 'health', '100216': 'construction and town planning',
                '100217': 'education', '100218': 'teaching', '100219': 'organisation of teaching',
                '100220': 'documentation', '100221': 'communications',
                '100222': 'information and information processing',
                '100223': 'information technology and data processing', '100224': 'natural and applied sciences',
                '100225': 'humanities', '100226': 'business organisation', '100227': 'business classification',
                '100228': 'legal form of organisations', '100229': 'management', '100230': 'accounting',
                '100231': 'competition', '100232': 'employment', '100233': 'labour market',
                '100234': 'organisation of work and working conditions',
                '100235': 'personnel management and staff remuneration', '100236': 'labour law and labour relations',
                '100237': 'transport policy', '100238': 'organisation of transport', '100239': 'land transport',
                '100240': 'maritime and inland waterway transport', '100241': 'air and space transport',
                '100242': 'environmental policy', '100243': 'natural environment',
                '100244': 'deterioration of the environment', '100245': 'agricultural policy',
                '100246': 'agricultural structures and production', '100247': 'farming systems',
                '100248': 'cultivation of agricultural land', '100249': 'means of agricultural production',
                '100250': 'agricultural activity', '100251': 'forestry', '100252': 'fisheries',
                '100253': 'plant product', '100254': 'animal product', '100255': 'processed agricultural produce',
                '100256': 'beverages and sugar', '100257': 'foodstuff', '100258': 'agri-foodstuffs',
                '100259': 'food technology', '100260': 'production', '100261': 'technology and technical regulations',
                '100262': 'research and intellectual property', '100263': 'energy policy',
                '100264': 'coal and mining industries', '100265': 'oil industry',
                '100266': 'electrical and nuclear industries', '100267': 'soft energy',
                '100268': 'industrial structures and policy', '100269': 'chemistry',
                '100270': 'iron, steel and other metal industries', '100271': 'mechanical engineering',
                '100272': 'electronics and electrical engineering', '100273': 'building and public works',
                '100274': 'wood industry', '100275': 'leather and textile industries',
                '100276': 'miscellaneous industries', '100277': 'Europe', '100278': 'regions of EU Member States',
                '100279': 'America', '100280': 'Africa', '100281': 'Asia and Oceania', '100282': 'economic geography',
                '100283': 'political geography', '100284': 'overseas countries and territories',
                '100285': 'United Nations', '100286': 'European organisations',
                '100287': 'extra-European organisations', '100288': 'world organisations',
                '100289': 'non-governmental organisations'}
}

MESH_CONCEPTS = {
    "level_1": {'A': ('Anatomy', 'Anatomy'),
                'B': ('Organisms', 'Organisms'),
                'C': ('Diseases', 'Diseases'),
                'D': ('Chemicals and Drugs', 'Drugs'),
                'E': ('Analytical, Diagnostic and Therapeutic Techniques, and Equipment', 'Technical'),
                'F': ('Psychiatry and Psychology', 'Psychology'),
                'G': ('Phenomena and Processes', 'Processes'),
                'H': ('Disciplines and Occupations', 'Occupations'),
                'I': ('Anthropology, Education, Sociology, and Social Phenomena', 'Anthropology'),
                'J': ('Technology, Industry, and Agriculture', 'Industry'),
                'K': ('Humanities', 'Humanities'),
                'L': ('Information Science', 'Information'),
                'M': ('Named Groups', 'Groups'),
                'N': ('Health Care', 'Health Care'),
                'V': ('Publication Characteristics', 'Publications'),
                'Z': ('Geographicals', 'Geography'),
                },
    'level_2': {'A01': 'Body Regions', 'A02': 'Musculoskeletal System', 'A03': 'Digestive System',
                'A04': 'Respiratory System', 'A05': 'Urogenital System', 'A06': 'Endocrine System',
                'A07': 'Cardiovascular System', 'A08': 'Nervous System', 'A09': 'Sense Organs', 'A10': 'Tissues',
                'A11': 'Cells', 'A12': 'Fluids and Secretions', 'A13': 'Animal Structures',
                'A14': 'Stomatognathic System', 'A15': 'Hemic and Immune Systems', 'A16': 'Embryonic Structures',
                'A17': 'Integumentary System', 'A18': 'Plant Structures', 'A19': 'Fungal Structures',
                'A20': 'Bacterial Structures', 'A21': 'Viral Structures', 'B01': 'Eukaryota', 'B02': 'Archaea',
                'B03': 'Bacteria', 'B04': 'Viruses', 'B05': 'Organism Forms', 'C01': 'Infections', 'C04': 'Neoplasms',
                'C05': 'Musculoskeletal Diseases', 'C06': 'Digestive System Diseases', 'C07': 'Stomatognathic Diseases',
                'C08': 'Respiratory Tract Diseases', 'C09': 'Otorhinolaryngologic Diseases',
                'C10': 'Nervous System Diseases', 'C11': 'Eye Diseases', 'C12': 'Urogenital Diseases',
                'C13': 'Female Genital Diseases and Pregnancy Complications', 'C14': 'Cardiovascular Diseases',
                'C15': 'Hemic and Lymphatic Diseases',
                'C16': 'Congenital, Hereditary, and Neonatal Diseases and Abnormalities',
                'C17': 'Skin and Connective Tissue Diseases', 'C18': 'Nutritional and Metabolic Diseases',
                'C19': 'Endocrine System Diseases', 'C20': 'Immune System Diseases',
                'C21': 'Disorders of Environmental Origin', 'C22': 'Animal Diseases',
                'C23': 'Pathological Conditions, Signs and Symptoms', 'C24': 'Occupational Diseases',
                'C25': 'Chemically-Induced Disorders', 'C26': 'Wounds and Injuries', 'D01': 'Inorganic Chemicals',
                'D02': 'Organic Chemicals', 'D03': 'Heterocyclic Compounds', 'D04': 'Polycyclic Compounds',
                'D05': 'Macromolecular Substances', 'D06': 'Hormones, Hormone Substitutes, and Hormone Antagonists',
                'D08': 'Enzymes and Coenzymes', 'D09': 'Carbohydrates', 'D10': 'Lipids',
                'D12': 'Amino Acids, Peptides, and Proteins', 'D13': 'Nucleic Acids, Nucleotides, and Nucleosides',
                'D20': 'Complex Mixtures', 'D23': 'Biological Factors', 'D25': 'Biomedical and Dental Materials',
                'D26': 'Pharmaceutical Preparations', 'D27': 'Chemical Actions and Uses', 'E01': 'Diagnosis',
                'E02': 'Therapeutics', 'E03': 'Anesthesia and Analgesia', 'E04': 'Surgical Procedures, Operative',
                'E05': 'Investigative Techniques', 'E06': 'Dentistry', 'E07': 'Equipment and Supplies',
                'F01': 'Behavior and Behavior Mechanisms', 'F02': 'Psychological Phenomena', 'F03': 'Mental Disorders',
                'F04': 'Behavioral Disciplines and Activities', 'G01': 'Physical Phenomena',
                'G02': 'Chemical Phenomena', 'G03': 'Metabolism', 'G04': 'Cell Physiological Phenomena',
                'G05': 'Genetic Phenomena', 'G06': 'Microbiological Phenomena', 'G07': 'Physiological Phenomena',
                'G08': 'Reproductive and Urinary Physiological Phenomena',
                'G09': 'Circulatory and Respiratory Physiological Phenomena',
                'G10': 'Digestive System and Oral Physiological Phenomena',
                'G11': 'Musculoskeletal and Neural Physiological Phenomena', 'G12': 'Immune System Phenomena',
                'G13': 'Integumentary System Physiological Phenomena', 'G14': 'Ocular Physiological Phenomena',
                'G15': 'Plant Physiological Phenomena', 'G16': 'Biological Phenomena', 'G17': 'Mathematical Concepts',
                'H01': 'Natural Science Disciplines', 'H02': 'Health Occupations', 'I01': 'Social Sciences',
                'I02': 'Education', 'I03': 'Human Activities', 'J01': 'Technology, Industry, and Agriculture',
                'J02': 'Food and Beverages', 'J03': 'Non-Medical Public and Private Facilities', 'K01': 'Humanities',
                'L01': 'Information Science', 'M01': 'Persons', 'N01': 'Population Characteristics',
                'N02': 'Health Care Facilities, Manpower, and Services',
                'N03': 'Health Care Economics and Organizations', 'N04': 'Health Services Administration',
                'N05': 'Health Care Quality, Access, and Evaluation', 'N06': 'Environment and Public Health',
                'Z01': 'Geographic Locations'}

}

UKLEX_CONCEPTS = {'level_1': {'AGRICULTURE & FOOD': ('Agriculture & Food', 'agriculture'),
                              'CHILDREN': ('Children', 'children'),
                              'CRIMINAL LAW': ('Criminal Law', 'crime'),
                              'EDUCATION': ('Education', 'education'),
                              'ENVIRONMENT': ('Environment', 'environment'),
                              'EU': ('EU', 'european'),
                              'FINANCE': ('Finance', 'finance'),
                              'HEALTH CARE': ('Health Care', 'health'),
                              'HOUSING': ('Housing', 'housing'),
                              'IMMIGRATION & CITIZENSHIP': ('Immigration & Citizenship', 'immigration'),
                              'LOCAL GOVERNMENT': ('Local Government', 'local'),
                              'PLANNING & DEVELOPMENT': ('Planning & Development', 'planning'),
                              'POLITICS': ('Politics', 'politics'),
                              'PUBLIC ORDER': ('Public Order', 'public'),
                              'SOCIAL SECURITY': ('Social Security', 'social'),
                              'TAXATION': ('Taxation', 'taxation'),
                              'TELECOMMUNICATIONS': ('Telecommunications', 'telecommunications'),
                              'TRANSPORTATION': ('Transportation', 'transportation')},
                  'level_2': {'AGRICULTURE': ('Agriculture', 'agriculture'),
                              'AIR TRANSPORT': ('Air Transport', 'air transport'), 'ANIMALS': ('Animals', 'animals'),
                              'BANKING': ('Banking', 'banking'), 'BROADCASTING': ('Broadcasting', 'broadcasting'),
                              'CHILDREN': ('Children', 'children'), 'CITIZENSHIP': ('Citizenship', 'citizenship'),
                              'CRIMINAL LAW': ('Criminal Law', 'criminal law'), 'DEFENCE': ('Defence', 'defence'),
                              'DISABLED PERSONS': ('Disabled Persons', 'disabled persons'),
                              'EDUCATION': ('Education', 'education'), 'ELECTIONS': ('Elections', 'elections'),
                              'EMPLOYMENT': ('Employment', 'employment'), 'ENVIRONMENT': ('Environment', 'environment'),
                              'EU': ('Eu', 'eu'), 'FINANCE': ('Finance', 'finance'),
                              'FIRE AND RESCUE SERVICES': ('Fire And Rescue Services', 'fire and rescue services'),
                              'FOOD': ('Food', 'food'), 'HEALTH CARE': ('Health Care', 'health care'),
                              'HOUSING': ('Housing', 'housing'), 'IMMIGRATION': ('Immigration', 'immigration'),
                              'INSURANCE': ('Insurance', 'insurance'),
                              'LAND REGISTRATION': ('Land Registration', 'land registration'),
                              'LAND TRANSPORTATION': ('Land Transportation', 'land transportation'),
                              'LOCAL GOVERNMENT': ('Local Government', 'local government'), 'NHS': ('Nhs', 'nhs'),
                              'PLANNING': ('Planning', 'planning'), 'POLICE': ('Police', 'police'),
                              'POLITICAL PARTIES': ('Political Parties', 'political parties'),
                              'POLLUTION': ('Pollution', 'pollution'), 'PUBLIC ORDER': ('Public Order', 'public order'),
                              'SOCIAL SECURITY': ('Social Security', 'social security'),
                              'TAXATION': ('Taxation', 'taxation'),
                              'TELECOMMUNICATIONS': ('Telecommunications', 'telecommunications'),
                              'TERRORISM': ('Terrorism', 'terrorism'),
                              'TRANSPORT AND WORKS': ('Transport And Works', 'transport and works'),
                              'URBAN DEVELOPMENT': ('Urban Development', 'urban development'),
                              'WASTE': ('Waste', 'waste'), 'WATER': ('Water', 'water'),
                              'WATER TRANSPORT': ('Water Transport', 'water transport')}}
