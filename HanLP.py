# -*- coding:utf-8 -*-
from jpype import *
import os
import sys

reload(sys)
# 因为解码的时候会默认使用系统的编码，一般是ascii，如果是中文就会出现编码错误，直接将系统编码改成utf8则可
sys.setdefaultencoding('utf8')
path = os.getcwd();
# print(path)
startJVM(getDefaultJVMPath(), "-Djava.class.path="+path+"/hanlp-portable-1.3.4.jar:"+path+"/hanlp", "-Xms1g",
         "-Xmx1g")  # 启动JVM，Linux需替换分号;为冒号:
HanLP = JClass('com.hankcs.hanlp.HanLP')
# 中文分词
# print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
# testCases = [
#     "商品和服务",
#     "结婚的和尚未结婚的确实在干扰分词啊",
#     "买水果然后来世博园最后去世博会",
#     "中国的首都是北京",
#     "欢迎新老师生前来就餐",
#     "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
#     "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
# for sentence in testCases: print(HanLP.segment(sentence))

# 命名实体识别与词性标注
# NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
# print NLPTokenizer.segment('作为一个现代人，上网是我们很平常的一个行为，就像很多其他科技黑盒一样，我们不知道它是怎么运作的，如现在的智能手机，我们会用')

text = '''
简介

作为一个现代人，上网是我们很平常的一个行为，就像很多其他科技黑盒一样，我们不知道它是怎么运作的，如现在的智能手机，我们会用，但是根本不知道它是怎么运作起来的，我觉得这没关系，在社会分工越来越细的情况下，很多东西我们只能依靠专业人员，我们没办法弄通、弄懂所有东西，在这个知识量暴增的时代，这是不现实的，但是作为一个程序员，还是有必要明白一些基本的网络原理的，我学过一段时间网络，在网络工程专业中，网络是怎么连起来的是一个非常基础的问题，我原本是不想写的，但是每次跟舍友讨论问题时，特别是服务器连接方面的，就会因为底层知识不同而有比较大的分歧，所以我觉得写写

IP的真正作用

网络就像一个蜘蛛网，我们的信息流就在这蜘蛛网上穿行，但是这个网太大，太复杂了，如果没有什么措施，我们的信息流很可能迷路，然后失踪，这就意味着我们发送一条消息后，就石沉大海、了无音讯了，这当然是不好的，为了解决这个问题，就出现了IP，现在常见的有IPv4和IPv6，虽说IPv6是未来，但是现在很多企业并没有使用，这里的原因就多了，我觉得最大的原因就是成本。一看到IP，很多人就会觉得网络不就是通过IP来定位，然后将相应的消息发送给对方的吗？这种说法其实并不对，IP的作用很多时候只起导向作用，网络之间的信息的传递其实靠的是MAC地址（本篇只讨论以太网，非以太网是没有MAC地址的，如帧中继网络）。

不要懵，我来模拟一遍一个简单的消息传输过程，记住这是非常简化的一个过程，网络传递消息的过程中还牵连到很多路由协议、ACL控制等等

首先我们电脑A的IP是6.6.6.6/24（/24表示子网掩码是24位，子网掩码用于分割网络位和主机位），此时我们想发送给电脑B，IP为8.8.8.8/24，那么首先电脑A会将源地址，也就是自己的IP6.6.6.6，和目标地址8.8.8.8封装到自己的数据包里，这个一般在第三层完成（网络层），接着将自己的MAC地址（电脑A的MAC地址）和目标的MAC地址也封装到数据包里，这个在第二层完成（链路数据层），此时电脑A当然不知道电脑B的MAC地址，所以电脑A要发送广播，此时目标MAC地址填全f，来询问一下自己所在网段中是否存在电脑B，如果存在电脑B的MAC地址是多少，因为电脑B不在6.6.6.0网段，所以没有人会回应电脑A的广播报文，当电脑A接收不到回应的报文，它就会请求网关的MAC地址，网关当然会接收这个请求，并将自己的MAC地址返回给电脑A，此时电脑A就会将目标地址的MAC设为网关的MAC地址，此时数据包会根据目标MAC地址来选择要发送到哪里

当数据包到了网关后（网关其实就是边界路由的一个接口），就会进行路由寻址，因为路由器是三层设备，所以就会将数据包解包到第三层，从上一段的描述可以知道，数据包第三层封装着源IP和目标IP，路由器会通过路由表来匹配目标IP，通过最长匹配原则选择出该数据包要去的方向（也就是要从哪个接口出），确定了方向后，就会将刚刚解开的包再次封装，第三层源IP和目标IP都不改变，但是源MAC地址变成了路由器本身，目标MAC地址变成了下一跳的MAC地址，然后数据会根据目标MAC地址再次找到要去到的地方，一般又是一个路由器，同样，该路由器会执行相同的步骤，先将数据包解开封装，解到第三层，看它的目标IP，然后通过目标IP来查自己的路由表，通过最长匹配原则找到一个适合的下一跳（也就要往哪个接口出去），再将数据包封装，将源MAC地址变成自己，目标MAC地址变成下一跳

最终，数据包到达8.8.8.0的网关，然后网关直接将数据包发给对应的电脑，如果该网段中有很多设备，那路由器可能就会发给相应的交换机，路由器怎么发送数据包完全看该路由器中的路由表，当8.8.8.8，也就是电脑B收到电脑A发送过来的数据后，就会以同样的方式将响应数据发回给电脑A，数据有去有回，才是一个完成的通信

上面就是一个简单的网络中传输数据的过程，可以发现IP其真实的作用是一个方向，将目标的范围慢慢缩小，直到找到目标，可以打个现实中的例子，你的IP是中国广东广州海珠区，那么我找你就会先从全世界的范围收缩到中国，然后又从中国这个范围收缩到广东，接着收缩到广州接着是珠海区，然后就可以通过你的MAC来定位到具体的你，那MAC地址在这个现实例子中就是，我要从美国找到你，那么我要先去到中国，具体怎么去，看一下MAC地址，原来从纽约机场就可以出发到的北京机场，然后我再看IP，原来在广东广州，怎么去？同样通过MAC地址，发现可以做高铁，从北京高铁站到广州南站。再次强调，IP只是导向， 而MAC才是数据包具体要去的地址，从上面的描述，你可以明白，网络通信的过程是逐跳的

什么是最长匹配原则

没学过网络工程的人可能不清楚，所谓最长匹配原则其实就是字面上的意思，跟我最多相同的，就相互匹配，这个是路由器选择下条路由时使用的规则，下面举个例子
'''

# 关键词提取
# document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
#            "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
#            "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
#            "严格地进行水资源论证和取水许可的批准。"
# document = text

def GetKeyWord(content,number):
    return HanLP.extractKeyword(content,number)

def GetSummary(content,number):
    return HanLP.extractSummary(content,number)

def GetPhrase(content,number):
    return HanLP.extractPhrase(content, number)
# print HanLP.extractKeyword(document, 2)
# # 自动摘要
# print HanLP.extractSummary(document, 3)
# # 短语提取
# phraseList = HanLP.extractPhrase(text,10);
# print phraseList
# 依存句法分析
# print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))

def ShopJVM():
    shutdownJVM()
