# !/usr/bin/python
# -*- coding: utf-8 -*-

class MultidialogLabel:
    (Suite, Plan, Guide, Other) = ('Suite', 'Plan', 'Guide', 'Other')


class MultidialogPlan:
    (One, Two, Three) = ('套餐', '意外', '重疾')


class MultidialogProperties:
    (Relation, Age, Sex) = ('Relation', 'Age', 'Sex')


class Template(object):
    def __init__(self, client_id=None, second_round=None, plan=None):
        self.client_id = client_id
        self.second_round = second_round
        self.plan = plan

    def get_plan(self):
        return self.plan


# 套餐
class Insuree_0(Template):
    def __init__(self, relation=None, sex=None, age=None, social_benefit=None, maritial_status=None, income=None):
        # 区分是孩子方案，成人方案，还是老人方案
        self.relation = relation
        self.age = age
        self.social_benefit = social_benefit
        self.sex = sex
        self.maritial_status = maritial_status
        self.income = income

    def check_attributes(self, age):
        if age < 18:
            self.maritial_status = 'single'
            self.sex = 'N/A'
            self.income = 0
        elif age > 59:
            self.maritial_status = 'married'
            self.sex = 'N/A'
            self.income = 0
        else:
            pass


# 单品：意外
class Insuree_1(Template):
    def __init__(self, recreation=None, age=None, occupation=None):
        self.recreation = recreation
        self.age = age
        self.occupation = occupation


# 单品：重疾
class Insuree_2(Template):
    def __init__(self, health=None, age=None):
        self.health = health
        self.age = age


# 单品：医疗
class Insuree_3(Template):
    def __init__(self, social_benefit=None, age=None, address=None):
        self.social_benefit = social_benefit
        self.age = age
        self.address = address


# 单品：防癌
class Insuree_4(Template):
    def __init__(self, health=None, age=None):
        self.health = health
        self.age = age


# 单品：寿险
class Insuree_5(Template):
    def __init__(self, health=None, age=None):
        self.health = health
        self.age = age


# 单品：旅游
class Insuree_6(Template):
    def __init__(self, destination=None, length_of_stay=None, frequency=None):
        self.destination = destination
        self.length_of_stay = length_of_stay
        self.frequency = frequency


# 单品：教育
class Insuree_7(Template):
    def __init__(self, income=None, age=None):
        self.income = income
        self.age = age


# 单品：女性
class Insuree_8(Template):
    def __init__(self, health=None, age=None, occupation=None):
        self.health = health
        self.age = age
        self.occupation = occupation


templates = {
    '套餐': Insuree_0(),
    '意外': Insuree_1(),
    '重疾': Insuree_2(),
    '医疗': Insuree_3(),
    '防癌': Insuree_4(),
    '寿险': Insuree_5(),
    '旅游': Insuree_6(),
    '教育': Insuree_7(),
    '女性': Insuree_8(),
}

question_dict = {
    # 关系
    'relation': ['请问您为谁投保呢？(本人，父亲，母亲，爱人，儿子，女儿，朋友等)'],
    # 年龄
    'age': ['请问您%s的年龄是什么？', '请问您%s今年几岁？', '您%s贵庚？'],
    # 性别
    'sex': ['%s的法定性别呢？我是女', '%s是男还是女？', '请问%s的法定性别？'],
    # 收入
    'income': ['请问您%s的年总收入（税前）是多少？', '您%s每年收入是多少？', '您%s每年有多少收入？'],
    # 兴趣
    'recreation': ['您%s有什么兴趣爱好么？小狮妹我喜欢烧菜，旅游，看书', '您%s平常业余爱好是什么?'],
    # 职业
    'occupation': ['请问您%s是从事什么职业的？', '请问您%s的职业是什么？', '请问您%s是什么职业？'],
    # 健康状况
    'health': ['您%s有什么病例史么？'],
    # 社保
    'social_benefit': ['请问您%s有社保么？', '您%s有社保么？'],
    # 住址
    'address': ['请问您%s的现居地是哪里？小狮妹我住在北京', '请问您%s的现居地是啥？'],
    # 目的地
    'destination': ['您%s旅游的目的地是哪里呢？'],
    # 旅行时长
    'length_of_stay': ['您%s这次出去游玩多少天？'],
    # 旅行频率
    'frequency': ['您%s每年出游的频率是多少？'],
    # 婚姻状况
    'maritial_status': ['请问您%s是单身，已婚，还是离异？', '请问您%s目前的婚姻状况是什么？'],
}

recommendation_dict = {
    '套餐': {
        '少儿': {
            "title": {
                'user_id': '',
                'relation': ''
            },
            'plan': {
                'A': [
                    '社保优先',
                    '重疾险，保期30年，保额30万',
                    '意外险，保期1年，保额20万',
                    '医疗险，保期1年，保额50万',
                    '专项重疾险，保期1年，保额30万',
                    '教育金保险，保期30年，保额50万'
                ],
                'B': [
                    '社保优先',
                    '重疾险，保期30年，保额50万',
                    '意外险，保期1年，保额50万',
                    '医疗险，保期1年，保额50万',
                    '专项重疾险，保期1年，保额50万',
                    '教育金保险，保期30年，保额50万'
                ]
            },
            'coverage': ['200万', '230万'],
            'risk_chart': {
                'A': [
                    {
                        'name': '社保覆盖',
                        'evaluation': '其中社保可以为小孩覆盖基础医疗报销；但进口药、特殊药不纳入报销范围；',
                        'risk': 0
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '孩子的安全意识较低，更容易出现磕磕碰碰的情况，据统计中国每天150名儿童因意外失去生命；中国意外伤害占儿童身故总量的26.1%',
                        'risk': 0.30
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '儿童重疾发病率逐年攀升，成为了仅次于意外伤害的儿童第二杀手；世卫组织资料显示：中国0-14岁儿童的肿瘤发病率为19-89.9%每10万儿童，其中恶性肿瘤的发病率由以前的10.14%上升到了21.29%每10万。',
                        'risk': 0.23
                    },
                    {
                        'name': '住院医疗风险',
                        'evaluation': '0-14岁儿童的住院医疗险理赔案件中，有61.5%的理赔案件集中在0~6岁的低龄儿童，首当其冲的理赔原因是支气管炎和肺炎，其次手足口病、口腔性疱疹、发烧、肠胃炎也是儿童导致生病住院的风险因素；',
                        'risk': 0.30
                    },
                    {
                        'name': '教育风险',
                        'evaluation': '有统计83.4%父母认为子女培养成本非常高，超出能力；78.2％的家长没有为孩子教育做预算；',
                        'risk': 0.17
                    }
                ],
                'B': [
                    {
                        'name': '社保覆盖',
                        'evaluation': '其中社保可以为小孩覆盖基础医疗报销；但进口药、特殊药不纳入报销范围；',
                        'risk': 0
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '孩子的安全意识较低，更容易出现磕磕碰碰的情况，据统计中国每天150名儿童因意外失去生命；中国意外伤害占儿童身故总量的26.1%',
                        'risk': 0.30
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '儿童重疾发病率逐年攀升，成为了仅次于意外伤害的儿童第二杀手；世卫组织资料显示：中国0-14岁儿童的肿瘤发病率为19-89.9%每10万儿童，其中恶性肿瘤的发病率由以前的10.14%上升到了21.29%每10万。',
                        'risk': 0.28
                    },
                    {
                        'name': '住院医疗风险',
                        'evaluation': '0-14岁儿童的住院医疗险理赔案件中，有61.5%的理赔案件集中在0~6岁的低龄儿童，首当其冲的理赔原因是支气管炎和肺炎，其次手足口病、口腔性疱疹、发烧、肠胃炎也是儿童导致生病住院的风险因素；',
                        'risk': 0.21
                    },
                    {
                        'name': '教育风险',
                        'evaluation': '有统计83.4%父母认为子女培养成本非常高，超出能力；78.2％的家长没有为孩子教育做预算；',
                        'risk': 0.21
                    }
                ]
            },

            'key_points': [
                {
                    'name': '社保保障',
                    'evaluation': '建议优先为小孩上社保：城镇居民医疗保险社保可按一定比例报销住院医疗费、门急诊费用。',
                    'product': ['城镇居民医疗保险'],
                    'product_url': ['https://www.datebao.com']
                },
                {
                    'name': '意外险保障',
                    'evaluation': '方案要点：1.孩子的安全意识较低，更容易出现磕磕碰碰的情况，而意外医疗保障就是为这部分报销而设定，所以意外医疗保额高可优先考虑。2.意外医疗门诊是专针对因发生意外而就诊的门诊，但对因疾病所产生费用不在意外门诊报销范围，所以涵盖意外疾病门诊可优先考虑。3.意外身故保额要足，建议0-10岁保额20w，10-17岁保额50万优先',
                    'product': ['儿童意外险'],
                    'product_url': ['https://www.datebao.com/productshow/123']
                },
                {
                    'name': '重疾险保障',
                    'evaluation': '方案要点：1.儿童因年龄小体质差，重疾发病和成人不尽相同，所有少儿重疾覆盖少儿常见疾病，如重症手足口病、严重川崎病等可优先考虑。2.从保险产品的性质来说，消费性产品是纯粹的保障，是最接近保险成本的；所以少儿重疾选择，长期消费型产品可优先考虑。3.建议保额充足至少30万起。4. 专项加强选择高发高费用大病，如白血病',
                    'product': ['少儿长期重疾险'],
                    'product_url': ['https://www.datebao.com/productshow/398']
                },
                {
                    'name': '医疗险保障',
                    'evaluation': '方案要点：1.小孩抵抗力较弱，可优先考虑涵盖疾病门诊类医疗险。2.少儿医疗保险可优先考虑等待期较短，30天内的。3.从报销比例来说，建议免赔额低，1w以内，0免赔，自费药赔付比例高的产品。',
                    'product': ['随e保长期重疾险', '少儿白血病险[专项加强]'],
                    'product_url': ['https://www.datebao.com', 'https://www.datebao.com/productshow/171']
                },
                {
                    'name': '教育金保障',
                    'evaluation': '1. 关注每个求学阶段的教育金保障。2. 投保人豁免优先',
                    'product': ['信诚金色年华教育金'],
                    'product_url': ['https://www.datebao.com']
                }
            ]
        },

        '成人未婚': {
            "title": {
                'user_id': '',
                'relation': ''
            },
            'plan': [
                '社保优先',
                '意外险，保期1年，',
                '重疾险，保期30年，',
                '中端医疗险，保期1年，',
                '寿险，保期30年，'
            ],
            'coverage': [],
            'risk_chart': {
                'A': [
                    {
                        'name': '社保保障',
                        'evaluation': '社保缴纳，可获得基础医疗保障，为养老提前做储蓄，但仅仅为基础保障，建议条件允许的情况下，还是补充一些商业保险。',
                        'risk': 0
                    },
                    {
                        'name': '门诊住院风险',
                        'evaluation': '据中国意外事故数据统计，年轻人为意外发生率最高的人群，尤其是18-25岁，身体虽好但意外难防。意外致死每10万人发生率为18.2%。',
                        'risk': 0.21
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '卫生部数据统计，人一生罹患重疾的几率高达72.18%，其中10个健康男性中3个会在65岁前得重疾、10个健康女性中2个会在65岁前得重疾。',
                        'risk': 0.27
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '据男性就医调查显示，53%的男性患男科疾病选择自己查些资料，药店买药自行医治。在2000名被调查的男性中，去公立医院占18%，考虑到面子问题到小医院或小诊所治疗的占26%，认为难以启齿不去治疗的占3%，可见男性就医率有多低。',
                        'risk': 0.25
                    },
                    {
                        'name': '寿险',
                        'evaluation': '',
                        'risk': 0.22
                    }
                ],
                'B': [
                    {
                        'name': '社保保障',
                        'evaluation': '社保缴纳，可获得基础医疗保障，为养老提前做储蓄，但仅仅为基础保障，建议条件允许的情况下，还是补充一些商业保险。',
                        'risk': 0
                    },
                    {
                        'name': '门诊住院风险',
                        'evaluation': '据中国意外事故数据统计，年轻人为意外发生率最高的人群，尤其是18-25岁，身体虽好但意外难防。意外致死每10万人发生率为18.2%。',
                        'risk': 0.21
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '卫生部数据统计，人一生罹患重疾的几率高达72.18%，其中10个健康男性中3个会在65岁前得重疾、10个健康女性中2个会在65岁前得重疾。',
                        'risk': 0.23
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '据男性就医调查显示，53%的男性患男科疾病选择自己查些资料，药店买药自行医治。在2000名被调查的男性中，去公立医院占18%，考虑到面子问题到小医院或小诊所治疗的占26%，认为难以启齿不去治疗的占3%，可见男性就医率有多低。',
                        'risk': 0.33
                    },
                    {
                        'name': '寿险',
                        'evaluation': '',
                        'risk': 0.23
                    }
                ]
            },
            'key_points': [
                {
                    'name': '社保保障',
                    'evaluation': '这个时期，身体虽好，但意外风险较大，没有社保，一旦出险，会造成较大财务缺口；建议先上社保，获得基础医疗保障，在经济条件较好的情况下，补充一些商业保险。',
                    'product': ['城镇社会保险', '养老保险和农村合作医疗保险'],
                    'product_url': ['https://www.datebao.com']
                },
                {
                    'name': '意外险保障',
                    'evaluation': '方案要点：1.这个时期为意外险发生率最高的一个时期，而意外保障的本质就是对发生意外的医疗费用进行报销，所以医疗保障较高的产品可优先考虑。2.猝死作为意外保险保障的一个盲区，很多意外产品保障不会包含在内，但猝死作为病魔之首，事件频发，所以涵盖猝死意外责任可优先考虑。3.意外险只投保狭义的“意外伤害保险”，而生病住院费用或不能赔付，所以涵盖综合意外保险责任的产品可优先考虑。 ',
                    'product': ['泰康个人意外险'],
                    'product_url': ['https://m.jssclub.com/product/show/511?agent_code=17de9e3']
                },
                {
                    'name': '重疾险保障',
                    'evaluation': '方案要点：1.重疾险购买的本质就是罹患重疾可获得最大保障，所以保额一定要充足，但想要获得最大保障杠杆，建议保费低、保额高产品可优先考虑。 2.这个时期一般身体状况良好，重疾风险相对较小，但处于长远考虑，50岁以后费率升高，保费倒挂，建议这个时期长期保障性重疾可优先考虑。3.购买保险，想要获得更大保障，一是看保额，还有一个就是保障时间；一定保障时间内，等待期越短，获得保障时间会更长一些，所以等待期短的重疾险可优先考虑。4.这个时期为人生的一个单身时期，大多初入职场，有一个共同的特点就是没钱，所以纯消费性重疾险可优先考虑。',
                    'product': ['和谐健康成人长期重疾险'],
                    'product_url': ['https://www.datebao.com/productshow/401']
                },
                {
                    'name': '医疗险保障',
                    'evaluation': '方案要点：1.医疗保险的本质就是对医疗费用进行报销，充足的保额可获得更多出险赔付，所以高保额医疗险可优先考虑。2.医疗险购买，等待期越短，一定保障时期内，获得的保障时间更长一些，所以等待期短的医疗险可优先考虑。3.基本医疗保险多报销社保内用药，但一些昂贵并对疾病有效的药是不予报销的，所以医疗险选择，可涵盖自费药、进口药、靶向药的产品可优先考虑。4.门诊医疗具有发病率高，理赔几率较大的特点，但为转嫁运营成本，市面很多产品不会覆盖，所以覆盖门诊医疗产品可优先考虑；这个时期为意外高发时期，建议覆盖意外责任的可优先考虑。',
                    'product': ['国寿e保百万医疗险'],
                    'product_url': ['https://m.jssclub.com/product/show/277?agent_code=17de9e3']
                },
                {
                    'name': '寿险保障',
                    'evaluation': '1.寿险作为责任险，高保障或是关键，这个时期建议定期保障型寿险可优先考虑。2.寿险作为以生存或死亡为给付条件的人身保险，想要保障杠杆最大化，建议（保费低，保障高）产品优先考虑。',
                    'product': ['弘康大白定期寿险'],
                    'product_url': ['https://www.datebao.com']
                }
            ]
        },

        '成人已婚': {
            "title": {
                'user_id': '',
                'relation': ''
            },
            'plan': [
                '社保优先',
                '寿险，保期30年，',
                '重疾险，保期终身，',
                '意外险，保期1年，',
                '中端医疗险，保期1年，',
                '专项女性险，保期1年，'
            ],
            'coverage': [],
            'risk_chart': {
                'A': [
                    {
                        'name': '社保保障',
                        'evaluation': '社保缴纳，可获得基础医疗保障，为养老提前做储蓄，但仅仅为基础保障，建议条件允许的情况下，还是补充一些商业保险。',
                        'risk': 0
                    },
                    {
                        'name': '寿险',
                        'evaluation': '据男性身故数据显示，19-50岁为身故高发的年龄段，占比高达78.07%。其中30-40岁发生频率最高。其中猝死超过交通事故、恶性肿瘤位列首因。',
                        'risk': 0.20
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '已婚男性面临家庭上老下小和事业攀升的双重压力，据数据显示，39岁以下恶性肿瘤发病率相对较低，但40岁以后开始迅速升高，40岁发病率是20岁发病率的7.45倍。',
                        'risk': 0.40
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '据保险理赔案件分析，男性意外出险占比高达75.54%，并且男性发生意外频率更高，出险率为女生2倍！从年龄来说，25-29岁区间的被保人出险率是最高的。',
                        'risk': 0.27
                    },
                    {
                        'name': '门诊住院医疗风险',
                        'evaluation': '据男性健康调查临床数据显示，男性看病的频率仅是女性的1/6，90%的男性表示没有健康体检的意识和习惯，80％的重病男性患者承认是因为长期不就医，才把小病养成大病，以致错过早期最佳治疗时期。',
                        'risk': 0.13
                    }
                ],
                'B': [
                    {
                        'name': '社保保障',
                        'evaluation': '社保缴纳，可获得基础医疗保障，为养老提前做储蓄，但仅仅为基础保障，建议条件允许的情况下，还是补充一些商业保险。',
                        'risk': 0
                    },
                    {
                        'name': '寿险',
                        'evaluation': '据男女寿命统计，女性比男性寿命平均长5-10岁；但对于已婚女性来说，肩负着生儿育女和家庭双重责任，一旦重疾或意外身故，对家庭的影响是非常大的，所以为已婚女性配置一款寿险产品是很有必要的。',
                        'risk': 0.20
                    },
                    {
                        'name': '重大疾病风险',
                        'evaluation': '乳腺癌作为女性健康首要杀手，发病率全世界排第一，据数据显示每10万人中有43位乳腺癌患者，每年新增病例约21万，死亡率为每10万人中有10位乳腺癌患者死亡。',
                        'risk': 0.40
                    },
                    {
                        'name': '意外伤害风险',
                        'evaluation': '据意外保险理赔案件统计分析，女性意外出险占达24.46%。风控分析得知，女性更关注自身安全，更多的是“享受”美景和购物的乐趣。',
                        'risk': 0.24
                    },
                    {
                        'name': '门诊住院医疗风险',
                        'evaluation': '已婚女性腺癌、宫颈癌等重疾风险大大升高，但女性风险意识相对较强，对自己身体显得更加“自爱”，所以定期体检和就医频率远高于男性。',
                        'risk': 0.16
                    }
                ]
            },
            'key_points': [
                {
                    'name': '社保保障',
                    'evaluation': '这个时期处于家庭搭建的初期，需要承担家庭的主要经济来源，建议先上社保，提供基础医疗保障，在经济条件允许的条件下，补充一些商业保险。',
                    'product': ['城镇社会保险', '养老保险和农村合作医疗保险'],
                    'product_url': ['https://www.datebao.com/']
                },
                {
                    'name': '寿险保障',
                    'evaluation': '方案要点：1.寿险根据保障期限的划分，可分为定期和终身；定寿和终身寿险费率相差较大，其中定寿具有保费低保障高的优点，所以定期保障性寿险可优先考虑。2.这个年龄段，多已搭建家庭，家庭责任和风险意识变强，作为家庭经济支柱，想要保障杠杆最大化，建议保费低，保障高产品可优先考虑。',
                    'product': ['弘康大白定期寿险'],
                    'product_url': ['https://www.datebao.com/']
                },
                {
                    'name': '重疾险保障',
                    'evaluation': '方案要点：1.重疾险根据性质划分，可分为纯保障型和储蓄型；相比之下，纯保障型重疾保费较低，灵活性更强，所以纯消费性重疾可优先考虑。2.据数据了解，男性40岁以后，重疾发病率大大提升，随年龄增长，保费和核保限制都会增加，所有建议提前做好重疾规划，长期保障性重疾险可优先考虑。3.重疾险作为以特定重疾为保障项目的保险，一定保障时间内，等待期越短，可获得的保障时间或更长一些，所以等待期越短重疾险可优先考虑。',
                    'product': ['和谐健康成人长期重疾险'],
                    'product_url': ['https://www.datebao.com/productshow/401']
                },
                {
                    'name': '意外险保障',
                    'evaluation': '方案要点：1.意外作为家庭的三大风险之一，夫妻双方任一出险，都会对家庭造成很大的影响。意外医疗保障的高低直接影响着出险赔付的多少，所以医疗保障较高产品可优先考虑。2.这个时期处于家庭搭建初期和事业攀升期，来自工作生活的各种压力，致使猝死率飙升；而猝死作为意外险保障盲区，所以涵盖猝死意外责任产品可优先考虑。3.意外险作为家庭保障的金三角之一，夫妻双方无论是发生意外还是重疾，都会对家庭造成很大的影响，所以涵盖综合意外保险责任的意外险可优先考虑。',
                    'product': ['安心高额意外险'],
                    'product_url': ['https://m.jssclub.com/product/show/511?agent_code=17de9e3']
                },
                {
                    'name': '医疗险保障',
                    'evaluation': '方案要点：1.医疗保险的本质就是对医疗费用进行报销，充足的保额可获得的医疗保障或更大一些，所以高保额医疗险可优先考虑。2.等待期越短，一定保障时期内，获得的保障时间更长一些，所以等待期短的医疗险可优先考虑。3.基本医疗保险多报销社保内用药，但一些昂贵并对疾病有效的药是不予报销的，所以医疗险选择，可涵盖自费药、进口药、靶向药的产品可优先考虑。4.门诊医疗具有发病率高，理赔几率较大的特点，但为转嫁运营成本，市面很多产品不会覆盖，所以覆盖门诊医疗产品可优先考虑；这个时期为意外高发时期，建议覆盖意外责任的可优先考虑。',
                    'product': ['太享e保百万医疗险', '平安健康e生保'],
                    'product_url': ['https://www.datebao.com/productshow/313',
                                    'https://m.jssclub.com/product/show/230?agent_code=17de9e3']
                },
                {
                    'name': '女性险保障',
                    'evaluation': '方案要点：1.这个时期的女性肩负着生儿育女和家庭的双重责任，同时负担着工作岗位的职责，患病几率是远远高于男性，所以高保障女性险可优先考虑。2.女性由于身体的特殊构造，婚后妇科重疾发病率大大增加，所以覆盖女性常见多发病种产品可优先考虑。3.考虑到女性的爱美需求，建议覆盖因意外需接受整形保障的产品可优先考虑。',
                    'product': ['女性百万恶性肿瘤险'],
                    'product_url': ['https://www.datebao.com/productshow/327']
                }
            ]
        },

        '老人': {
            "title": {
                'user_id': '',
                'relation': ''
            },
            'plan': [
                '社保优先',
                '意外险，保期1年，保额30万',
                '防癌险，保期终身，保额50万'
            ],
            'coverage': ['80万'],
            'risk_chart': [
                {
                    'name': '社保覆盖',
                    'evaluation': '老人缴纳社保，可按一定比例报销门急诊费用和住院费用。不同地区的社保政策不同，至于收费情况以及报销比例请以当地政策为准。',
                    'risk': 0
                },
                {
                    'name': '意外伤害风险',
                    'evaluation': '老年人随着年龄增高，生活自理能力下降，意外发生率逐年升高；据相关数据统计，我国每年至少有2500万60岁以上老年人发生跌倒损伤，75岁以上老年人跌倒与损伤的发生率则成倍增加。',
                    'risk': 0.45
                },
                {
                    'name': '防癌风险',
                    'evaluation': '随着社会老龄化的加剧，临床癌症患者占比大幅提升；据数据统计全国的恶性肿瘤患者中，50岁以上人群发病占全部发病的80%以上；60岁以上的老年人，癌症发病率超过1%，80岁达到高峰，也就是100个60岁以上的老人，就有一个得癌症。',
                    'risk': 0.34
                },
                {
                    'name': '其他',
                    'evaluation': '',
                    'risk': 0.21
                },
            ],
            'key_points': [
                {
                    'name': '社保保障',
                    'evaluation': '老人没有社保或没有基础保障，建议先为老人缴纳社保，在条件允许的情况下补充意外和防癌保障。',
                    'product': ['城镇社会保险', '养老保险和农村合作医疗保险'],
                    'product_url': ['https://www.datebao.com/', 'https://www.datebao.com/']
                },
                {
                    'name': '意外险保障',
                    'evaluation': '方案要点：1.老人随着年龄增高，生活自理能力的下降，意外发生概率大大提升，赔偿金额也相对较高，所以意外医疗高保额产品可优先考虑。2.60岁以上老人多已退休，但对于居家意外风险仍旧无法掌控，所以对于子女不在身边的居家老人，投保意外险涵盖救护车费用责任产品可优先考虑。3.老年人遭受意外伤害的概率大大高于其他年龄段，尤其日常生活中乘坐交通工具，出现意外、骨折/关节脱位等概率很高，所以覆盖其他交通工具意外的产品可优先考虑。',
                    'product': ['老年人意外综合险'],
                    'product_url': ['https://www.datebao.com/productshow/214']
                },
                {
                    'name': '防癌险保障',
                    'evaluation': '方案要点：1.防癌险选择首先要考虑保障范围和期限，像原位癌等轻症癌症一般花费较少，但也有特殊情况，而肿瘤一般花费较大，而有的防癌保险只承保肿瘤，而不承保轻症癌症，所以涵盖原位癌等轻症癌症可优先选择。2.防癌险涵盖完整发病率时期的产品可优先考虑。3.消费型防癌险，一般保险期限比较短，适合保费预算低、注重保障功能的人士。而长期储蓄型一般保费比较高，保险期限较长，如果年龄在35岁以上，经济条件不错，又比较注重储蓄，可优先考虑返还型产品。4.60岁以上老人癌症发病率逐渐升高，豁免保费功能就显得异常重要，所以防癌险涵盖豁免保费产品可优先考虑。',
                    'product': ['老年人防癌险'],
                    'product_url': ['https://m.jssclub.com/product/show/52?agent_code=17de9e3']
                },
            ]
        }
    },
    '意外': {
    },
    '重疾': {
    },
    '医疗': {
    },
    '防癌': {
    },
    '寿险': {
    },
    '旅游': {
    },
    '教育': {
    },
    '女性': {
    },

}

if __name__ == '__main__':
    value = Insuree_8()

    print(value.__dict__)
