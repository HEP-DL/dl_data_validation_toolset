<head>
</head>
<body>
% for index, file in enumerate(files):
  <div>
    ${file}
    <a href="files/${index}.html">Link to File</a>
  </div>
% endfor
</body>