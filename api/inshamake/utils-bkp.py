# # Create a ThreadPoolExecutor
# executor = ThreadPoolExecutor(max_workers=5)


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()

# async def pull_from_web(session, url):
#     try:
#         html = await fetch(session, url)
#         sup = BeautifulSoup(html, 'html.parser')
#         content_script = sup.find('script', type='application/ld+json')
#         if content_script:
#             json_cont = json.loads(content_script.string)
#             article_body = json_cont.get('articleBody', None)
#             article_title = json_cont.get('headline', None)
#             if article_body:
#                 # Run summarize in a separate thread
#                 loop = asyncio.get_event_loop()
#                 inshamake = await loop.run_in_executor(executor, partial(summarize(article_body)))
#                 return {
#                     "Title": article_title,
#                     "body": inshamake[0].get('summary_text')
#                 }
#     except Exception as e:
#         return f"enable to retrieve with {str(e)}"

# async def allArticle():
#     articles = []
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, root)
#         sup = BeautifulSoup(html, 'html.parser')
#         content_links = sup.find_all('div', class_="article-title")
#         if content_links:
#             tasks = []
#             for lin in content_links[6:11]:
#                 linkx = lin.find('a', href=True)
#                 if linkx:
#                     url = linkx['href']
#                     tasks.append(pull_from_web(session, url))
#             results = await asyncio.gather(*tasks)
#             for art in results:
#                 if art and "error" not in art:
#                     articles.append(art)
#                     # print(art)
#                     # print('\n')
#     return articles
