#-*- encoding:utf-8 -*-

"""
@author:Chenyu Wang
@file: tex_abstract.py
@time: 2019/03/13
@v1.0  基于图算法的文本摘要模型，相似度计算依赖相同字出现再句子中的次数。
"""

import sys
sys.path.append('./lib')

from time import time
import pandas as pd
import data_gen as dg
import autils
from textrank4zh import TextRank4Sentence


class Tex(object):
    def __init__(self):
        self.tr4s = TextRank4Sentence(delimiters=['\n'])

    def write2file(self,res,filename):
        with open(filename,'w') as f:
            f.write(res+'\n')

    def single_content(self,data,sum_size):
        # # Sentence segmentation
        t0=time()
        raw_con = dg.cont(data)
        raw_text = '\n'.join(raw_con)

        t1 = time()
        # print('using TextRank, data clean:{}s'.format(round(t1-t0,2)))

        self.tr4s.analyze(text=raw_text, lower=True, source='all_filters')

        t2 = time()
        # print('Run TextRank analyze:{}s'.format(round(t2-t1,2)))
        # for i in raw_con:
        #     print (i)
        tpl=[]
        sum_list=self.tr4s.get_key_sentences(num=sum_size)
        for i in sum_list:
            tpl.append((i['sentence'],i['index']))
            # ind_res.append(i['index'])
        res,ind_res=autils.sort_tuple_list(tpl)
        t3 = time()
        print('return sum_list:{}s'.format(round(t3-t2,2)))

        return res,ind_res


    def texs_live_proc(self,input_dict):
        raw_context=input_dict['content']
        sum_size =input_dict['return_size']
        print('Using TexRank !!')

        if isinstance(raw_context,str):
            # print("receiving single doc!")
            return self.single_content(raw_context,sum_size)
        elif isinstance(raw_context,list):
            # print("receiving multi doc!")
            raw_context = '\n'.join(raw_context)
            return self.single_content(raw_context,sum_size)
        else:
            print("Error the Context is not support! ONLY support Str or List of Str!")
            return None


if __name__=='__main__':
    df = pd.read_csv('lib/portal_news_part.csv')

    # cont_dict={}
    # cont_dict['content']=df.content.tolist()
    # cont_dict['return_size']=1

    cont_dict={}
    # cont_dict['content']=df.iloc[1].content
    cont_dict['content'] = '''经济观察网讯 3月5日上午9时，十三届全国人大二次会议在人民大会堂开幕，听取国务院总理李克强关于政府工作的报告，审查国务院关于2018年国民经济和社会发展计划执行情况与2019年国民经济和社会发展计划草案的报告，审查国务院关于2018年中央和地方预算执行情况与2019年中央和地方预算草案的报告。

一、2018年工作回顾

过去一年是全面贯彻党的十九大精神开局之年，是本届政府依法履职第一年。我国发展面临多年少有的国内外复杂严峻形势，经济出现新的下行压力。在以习近平同志为核心的党中央坚强领导下，全国各族人民以习近平新时代中国特色社会主义思想为指导，砥砺奋进，攻坚克难，完成全年经济社会发展主要目标任务，决胜全面建成小康社会又取得新的重大进展。

——经济运行保持在合理区间。国内生产总值增长6.6%，总量突破90万亿元。经济增速与用电、货运等实物量指标相匹配。居民消费价格上涨2.1%。国际收支基本平衡。城镇新增就业1361万人、调查失业率稳定在5%左右的较低水平。近14亿人口的发展中大国，实现比较充分就业至关重要。

——经济结构不断优化。消费拉动经济增长作用进一步增强。服务业对经济增长贡献率接近60%，高技术产业、装备制造业增速明显快于一般工业，农业再获丰收。单位国内生产总值能耗下降3.1%。质量和效益继续提升。

——发展新动能快速成长。嫦娥四号等一批重大科技创新成果相继问世。新兴产业蓬勃发展，传统产业加快转型升级。大众创业万众创新深入推进，日均新设企业超过1.8万户，市场主体总量超过1亿户。新动能正在深刻改变生产生活方式、塑造中国发展新优势。

——改革开放取得新突破。国务院及地方政府机构改革顺利实施。重点领域改革迈出新的步伐，市场准入负面清单制度全面实行，简政放权、放管结合、优化服务改革力度加大，营商环境国际排名大幅上升。对外开放全方位扩大，共建“一带一路”取得重要进展。首届中国国际进口博览会成功举办，海南自贸试验区启动建设。货物进出口总额超过30万亿元，实际使用外资1383亿美元、稳居发展中国家首位。

——三大攻坚战开局良好。防范化解重大风险，宏观杠杆率趋于稳定，金融运行总体平稳。精准脱贫有力推进，农村贫困人口减少1386万，易地扶贫搬迁280万人。污染防治得到加强，细颗粒物（PM2.5）浓度继续下降，生态文明建设成效显著。

——人民生活持续改善。居民人均可支配收入实际增长6.5%。提高个人所得税起征点，设立6项专项附加扣除税。加大基本养老、基本医疗等保障力度，资助各类学校家庭困难学生近1亿人次。棚户区住房改造620多万套，农村危房改造190万户。城乡居民生活水平又有新提高。

我们隆重庆祝改革开放40周年，深刻总结改革开放的伟大成就和宝贵经验，郑重宣示在新时代将改革开放进行到底的坚定决心，激励全国各族人民接续奋斗，再创新的历史伟业。

回顾过去一年，成绩来之不易。我们面对的是深刻变化的外部环境。经济全球化遭遇波折，多边主义受到冲击，国际金融市场震荡，特别是中美经贸摩擦给一些企业生产经营、市场预期带来不利影响。我们面对的是经济转型阵痛凸显的严峻挑战。新老矛盾交织，周期性、结构性问题叠加，经济运行稳中有变、变中有忧。我们面对的是两难多难问题增多的复杂局面。实现稳增长、防风险等多重目标，完成经济社会发展等多项任务，处理好当前与长远等多种关系，政策抉择和工作推进的难度明显加大。经过全国上下共同努力，我国经济发展在高基数上总体平稳、稳中有进，社会大局保持稳定。这再次表明，在中国共产党领导下，中国人民有战胜任何艰难险阻的勇气、智慧和力量，中国的发展没有过不去的坎。

一年来，我们深入贯彻以习近平同志为核心的党中央决策部署，坚持稳中求进工作总基调，统筹稳增长、促改革、调结构、惠民生、防风险，稳妥应对中美经贸摩擦，着力稳就业、稳金融、稳外贸、稳外资、稳投资、稳预期，主要做了以下工作。

一是创新和完善宏观调控，经济保持平稳运行。面对新情况新变化，我们坚持不搞“大水漫灌”式强刺激，保持宏观政策连续性稳定性，在区间调控基础上加强定向、相机调控，主动预调、微调。坚持实施积极的财政政策，着力减税降费、补短板调结构。下调增值税税率，扩大享受税收优惠小微企业范围，出台鼓励研发创新等税收政策。全年为企业和个人减税降费约1.3万亿元。优化财政支出结构，盘活财政存量资金，重点领域支出得到保障。坚持实施稳健的货币政策，引导金融支持实体经济。针对融资难融资贵问题，先后4次降低存款准备金率，多措并举缓解民营和小微企业资金紧张状况，融资成本上升势头得到初步遏制。及时应对股市、债市异常波动，人民币汇率基本稳定，外汇储备保持在3万亿美元以上。

二是扎实打好三大攻坚战，重点任务取得积极进展。制定并有序实施三大攻坚战三年行动方案。稳步推进结构性去杠杆，稳妥处置金融领域风险，防控地方政府债务风险，改革完善房地产市场调控机制。深入推进精准脱贫，加强扶贫力量，加大资金投入，强化社会帮扶，贫困地区自我发展能力稳步提高。全面开展蓝天、碧水、净土保卫战。优化能源和运输结构。稳妥推进北方地区“煤改气”“煤改电”。全面建立河长制、湖长制。化肥农药使用量实现双下降。加强生态环保督察执法。积极应对气候变化。

三是深化供给侧结构性改革，实体经济活力不断释放。加大“破、立、降”力度。推进钢铁、煤炭行业市场化去产能。实施稳投资举措，制造业投资、民间投资增速明显回升。出台促进居民消费政策。全面推进“互联网+”，运用新技术新模式改造传统产业。深入推进简政减税减费。取消一批行政许可事项，“证照分离”改革在全国推开，企业开办时间大幅压缩，工业生产许可证种类压减三分之一以上。“双随机、一公开”监管全面实施。清理规范各类涉企收费，推动降低用电、用网和物流等成本。深化“互联网+政务服务”，各地探索推广一批有特色的改革举措，企业和群众办事便利度不断提高。

四是深入实施创新驱动发展战略，创新能力和效率进一步提升。大力优化创新生态，调动各类创新主体积极性。深化科技管理体制改革，推进关键核心技术攻关，加强重大科技基础设施、科技创新中心等建设。强化企业技术创新主体地位，将提高研发费用加计扣除比例政策扩大至所有企业。制定支持双创深入发展的政策措施。技术合同成交额增长30%以上。

五是加大改革开放力度，发展动力继续增强。深化国资国企改革，国有企业优化重组、提质增效取得新进展。针对民营企业发展遇到的困难和问题，千方百计帮助解忧纾困。推进财税体制改革，预算绩效管理改革全面启动。改革金融监管体制，完善利率、汇率市场化形成机制。农业农村、社会事业、生态环保等领域改革不断深化。推出对外开放一系列重大举措。共建“一带一路”引领效应持续释放，同沿线国家的合作机制不断健全，经贸合作和人文交流加快推进。出台稳外贸政策，货物通关时间压缩一半以上。下调部分商品进口关税，关税总水平由9.8%降至7.5%。新设一批跨境电商综合试验区。复制推广自贸试验区改革经验。大幅压缩外资准入负面清单，扩大金融、汽车等行业开放，一批重大外资项目落地，新设外资企业增长近70%。

六是统筹城乡区域发展，良性互动格局加快形成。乡村振兴战略有力实施，粮食总产量保持在1.3万亿斤以上。新型城镇化扎实推进，近1400万农业转移人口在城镇落户。推进西部开发、东北振兴、中部崛起、东部率先发展，出台一批改革创新举措。京津冀协同发展取得明显进展，长江经济带生态优先、绿色发展格局不断巩固。粤港澳大湾区规划建设迈出实质性步伐，港珠澳大桥建成通车。加大对革命老区、民族地区、边疆地区、贫困地区改革发展支持力度。新增高速铁路运营里程4100公里，新建改建高速公路6000多公里、农村公路30多万公里。城乡区域发展协调性持续增强。

七是坚持在发展中保障和改善民生，改革发展成果更多更公平惠及人民群众。针对外部环境变化给就业带来的影响，及时出台稳就业举措。大力推动义务教育教师工资待遇政策落实，加强乡村小规模学校和乡镇寄宿制学校建设。建立企业职工基本养老保险基金中央调剂制度，提高退休人员基本养老金，城乡居民基础养老金最低标准从每月70元提高到88元。继续提高优抚、低保等标准，残疾人“两项补贴”惠及所有符合条件人员。加强退役军人服务管理工作，维护退役军人合法权益。深化医疗、医保、医药联动改革。稳步推进分级诊疗。提高居民基本医保补助标准和大病保险报销比例。加快新药审评审批改革，17种抗癌药大幅降价并纳入国家医保目录。加快推进文化惠民工程，持续加强基层公共文化服务。全民健身蓬勃开展，体育健儿在国际大赛上再创佳绩。

八是推进法治政府建设和治理创新，保持社会和谐稳定。提请全国人大常委会审议法律议案18件，制定修订行政法规37部。改革调整政府机构设置和职能配置。深入开展国务院大督查，推动改革发展政策和部署落实。发挥审计监督作用。改革完善城乡基层治理。创新信访工作方式。改革和加强应急管理，及时有效应对重大自然灾害，生产安全事故总量和重特大事故数量继续下降。加强食品药品安全监管，严厉查处长春长生公司等问题疫苗案件。健全国家安全体系。强化社会治安综合治理，开展扫黑除恶专项斗争，依法打击各类违法犯罪，平安中国建设取得新进展。

认真贯彻党中央全面从严治党战略部署，加强党风廉政建设。推进“两学一做”学习教育常态化制度化。严格落实中央八项规定及其实施细则精神，坚定不移纠正“四风”。严肃查处各类违法违规行为，惩处腐败分子，反腐败斗争取得压倒性胜利。

过去一年，中国特色大国外交取得新成就。成功举办博鳌亚洲论坛年会、上合组织青岛峰会、中非合作论坛北京峰会等重大主场外交活动。习近平主席等国家领导人出访多国，出席亚太经合组织领导人非正式会议、二十国集团领导人峰会、金砖国家领导人会晤、亚欧首脑会议、东亚合作领导人系列会议等重大活动。同主要大国关系总体稳定，同周边国家关系全面发展，同发展中国家团结合作纽带更加牢固。推动构建新型国际关系，推动构建人类命运共同体。坚定维护国家主权、安全、发展利益。经济外交、人文交流成果丰硕。中国致力于促进世界和平与发展，作出了世人共睹的重要贡献。
    '''
    cont_dict['return_size'] = 5

    time1=time()
    textrk = Tex()
    test=textrk.texs_live_proc(cont_dict)
    print("Total time cost:{0}s , result:{1}".format(round(time()-time1,2),test))
