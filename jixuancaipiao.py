"""机选彩票的函数"""

from random import choice
from random import sample

def jixuancp(n):
	"""玩家机选的彩票"""
	jx_caipiaos = {}
	touzhushu = ["机选彩票"+v for v in ([str(i) for i in range(1,n+1)])]

	for touzhu in touzhushu:
		jx_caipiao = sample(range(1,34),6) + [choice(range(1,17))]
		jx_caipiaos[touzhu] = jx_caipiao

	print(jx_caipiaos)
