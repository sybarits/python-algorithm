import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Node A1", "Node A2", "Node B1", "Node B2", "Node C1", "Node C2"],  # 노드의 라벨
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3],  # 각 링크의 출발 노드 인덱스
      target = [2, 3, 3, 4, 4, 5],  # 각 링크의 도착 노드 인덱스
      value = [8, 4, 2, 8, 4, 2]    # 각 링크의 두께를 결정하는 값
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()