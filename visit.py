import requests, os, re
from concurrent.futures import ThreadPoolExecutor

class Visit:
	def __init__(self):
		self.url = "https://camo.githubusercontent.com/c33b9df4c8924cb477f438935a7b74c08caf6e8718db97fe73e50a5aec22b793/68747470733a2f2f76697369746f722d62616467652e6665726969726177616e6e2e7265706c2e636f3f757365726e616d653d6734727a6b267265706f3d6734727a6b266c6162656c3d56697369746f72267374796c653d736f6369616c26636f6c6f723d25323334353742464626636f6e74656e74547970653d737667"
		self.mulai()
	
	def mulai(self):
		with ThreadPoolExecutor(max_workers=30) as th:
			for i in range(10000):
				th.submit(self.auto, i)
	
	def auto(self, i):
		try:
			a = requests.get(self.url, timeout=15)
			total = re.search('<text x="96" y="15" fill="#010101" fill-opacity=".3">(\d+)</text>', str(a.text)).group(1)
			print(f"[{i}]=> {total}")
		except Exception as e:
			pass

if __name__ == "__main__":
	os.system("clear")
	Visit()
