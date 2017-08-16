<%inherit file="base.mako"/>

<%block name="body_content">
<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h1>${top_report.name}</h1>
    </div>
  <div class='col-md-1'></div>    
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h2>Data Groups</h2>
    <table class="table table-hover">
    <tr>
    <th>Group</th><th>Number of Files</th><th>Number of Valid Files</th><th>Link</th>
    </tr>

    % for index, group in enumerate(top_report.groups):
      <tr>
        <td>${group.name}</td>
        <td>${group.n_files}</td>
        <td>${group.n_valid_files}</td>
        <td>
          <a href="${group.name}/index.html">Link to Group Report</a>
        </td>
      </tr>
    % endfor
    </table>
  </div>
  <div class='col-md-1'></div>
</div>

</%block>
