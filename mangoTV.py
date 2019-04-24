# -*- coding: utf-8 -*-

import time
import uiautomator2 as u2
import sys

rank = sys.argv[1]
device_num = sys.argv[2]
isOnlySign = sys.argv[3]

d = u2.connect(str(device_num))
try:
	print(d.info)
except:
	print("Connection Error")

if (d(text=u"芒果TV").exists):
	d(text=u"芒果TV").click()
	while (not d(text=u"精选").exists):
		time.sleep(1)

input_path = "account.txt"

account_list = []
password_list = []
with open(input_path, 'r') as fin:
	for lines in fin.readlines():
		account_list.append(lines.strip().split("/")[0])
		password_list.append(lines.strip().split("/")[1])

for i in range(len(account_list)):
	account = str(account_list[i])
	password = str(password_list[i])
	d(resourceId="com.hunantv.imgo.activity:id/img_click", className="android.view.View", instance=4).click()
	time.sleep(0.5)
	if (not d(text=u"立即登录").exists):
		d(scrollable=True).scroll.toEnd()
		time.sleep(0.5)
		d(resourceId="com.hunantv.imgo.activity:id/title", text=u"设置").click()
		time.sleep(3)
		d(scrollable=True).scroll.toEnd()
		time.sleep(0.5)
		d(resourceId="com.hunantv.imgo.activity:id/tvTitle", text=u"退出登录").click()
		while (not d(text=u"立即登录").exists):
			time.sleep(1)
	time.sleep(1)
	d(resourceId="com.hunantv.imgo.activity:id/tvNickname").click()
	time.sleep(0.5)
	if (d(resourceId="com.hunantv.imgo.activity:id/ivSwitchMode").exists):
		d(resourceId="com.hunantv.imgo.activity:id/ivSwitchMode").click()
	elif (d(text=u"账号密码登录").exists):
		d(text=u"账号密码登录").click()
	time.sleep(1)
	print("Using account: ", account)
	d(resourceId="com.hunantv.imgo.activity:id/etContent").set_text(account)
	d(resourceId="com.hunantv.imgo.activity:id/etContent", text=u"请输入密码").set_text(password)
	time.sleep(0.3)
	d.press("back")
	time.sleep(0.3)
	d(resourceId="com.hunantv.imgo.activity:id/btnLogin").click()
	while (not d(text=u"我的消息").exists):
		time.sleep(1)
	time.sleep(3)
	d(resourceId="com.hunantv.imgo.activity:id/tvCheckIn").click()
	time.sleep(3)
	d.press("back")
	# while (not d(description=u"积分商城").exists):
	# 	time.sleep(1)
	print (u"账号 ", account, u" 签到成功")
	# d.press("back")
	if (d(resourceId="com.hunantv.imgo.activity:id/ivLeft").exists):
		d(resourceId="com.hunantv.imgo.activity:id/ivLeft").click()
	time.sleep(1)

	if (str(isOnlySign) == "0"):
		d(resourceId="com.hunantv.imgo.activity:id/img_click", className="android.view.View", instance=2).click()
		time.sleep(1)
		if (d(resourceId="com.hunantv.imgo.activity:id/vClosePromotionView").exists):
			d(resourceId="com.hunantv.imgo.activity:id/vClosePromotionView").click()
			time.sleep(0.5)
		while (not d(resourceId="com.hunantv.imgo.activity:id/tvTitle", text=u"我的钱包").exists):
			d(resourceId="com.hunantv.imgo.activity:id/img_click", className="android.view.View", instance=2).click()
			time.sleep(3)
		while (not d(text=u"《少年可期》VIP首席大弟子 由你来定！").exists()):
			time.sleep(0.5)
		d(text=u"《少年可期》VIP首席大弟子 由你来定！").click();
		# d(resourceId="com.hunantv.imgo.activity:id/tvTitle", text=u"少年可期").click()
		time.sleep(5)
		while (not d(description=u"全部给Ta").exists):
			d.press("back")
			while (not d(text=u"《少年可期》VIP首席大弟子 由你来定！").exists()):
				time.sleep(0.5)
			d(text=u"《少年可期》VIP首席大弟子 由你来定！").click();
			time.sleep(5)

		if str(rank) == "1":
			d(description=u"全部给Ta").click()
			time.sleep(1)
			if d(description=u"您还不是会员，仅限会员参与哦~").exists:
				d(description=u"close").click()
				time.sleep(1)
			elif (d(descriptionContains=u"丁泽仁").exists):
				d(description=u"确认 ").click()
				print (u"账号 ", account, u" 投票成功")
				time.sleep(0.5)
			elif (d(description=u"青春值不够，购买专属礼品卡投更多！").exists):
				d(description=u"close").click()
				time.sleep(0.5)
			else:
				print(u"没把票投给丁泽仁，请检查排名输入是否正确，如果正确，速速联系开发者")
		else:
			while (not d(description="ec4abde2626c11e9a7f2ecf4bbc30ba4").sibling(className="android.view.View").child(description="btn_vote_all").exists):
				d.swipe(0.700, 0.880, 0.700, 0.660)
				time.sleep(1)
			time.sleep(0.5)
			d(description="ec4abde2626c11e9a7f2ecf4bbc30ba4").sibling(className="android.view.View").child(description="btn_vote_all").click()
			time.sleep(1.5)
			while (not d(description=u"您还不是会员，仅限会员参与哦~").exists and not d(description=u"确认 ").exists and not d(description=u"青春值不够，购买专属礼品卡投更多！").exists):
				d(description="ec4abde2626c11e9a7f2ecf4bbc30ba4").sibling(className="android.view.View").child(description="btn_vote_all").click()
				time.sleep(1)
			if (d(description=u"您还不是会员，仅限会员参与哦~").exists):
				d(description=u"close").click()
				time.sleep(0.5)
			elif (d(description=u"即将投5票给丁泽仁").exists):
				d(description=u"确认 ").click()
				print (u"账号 ", account, u" 投票成功")
				time.sleep(0.5)
			elif (d(description=u"青春值不够，购买专属礼品卡投更多！").exists):
				d(description=u"close").click()
				time.sleep(0.5)
			else:
				print(u"没把票投给丁泽仁，请检查排名输入是否正确，如果正确，速速联系开发者")
		time.sleep(0.5)
		d.press("back")
		time.sleep(0.5)
		d(resourceId="com.hunantv.imgo.activity:id/img_click", className="android.view.View", instance=4).click()
		time.sleep(0.5)

	d(scrollable=True).scroll.toEnd()
	time.sleep(0.5)
	d(resourceId="com.hunantv.imgo.activity:id/title", text=u"设置").click()
	time.sleep(0.5)
	d(scrollable=True).scroll.toEnd()
	time.sleep(0.5)
	d(resourceId="com.hunantv.imgo.activity:id/tvTitle", text=u"退出登录").click()
	while (not d(text=u"立即登录").exists):
		time.sleep(1)
	time.sleep(1)



