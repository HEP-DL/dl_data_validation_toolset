<%inherit file="base.mako"/>
<%block name="body_content">

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h1>Group Report For: ${group_report.name}</h1>
    <h3>Directory: ${group_report.directory} <h3>
    </div>
  <div class='col-md-1'></div>
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
  <h2>Files</h2>
  <table class="table table-hover">
    <tr>
    <th>File Name</th><th>Link</th><th>Valid</th>
    </tr>
  % for  file in group_report.file_reports:
      <tr
        %if file.valid:
        class="success"
        %else:
        class="danger"
        %endif
      >

        <td>
          ${file.file}
        </td>
        <td>
          <a href="${file.slug}/index.html">Link to File Report</a>
        </td>
        <td>
          %if file.valid:
            Valid
          %else:
            Invalid
          %endif
        </td>
      </tr>
    % endfor
    </table>
  </div>
  <div class='col-md-1'></div>
</div>

</%block>