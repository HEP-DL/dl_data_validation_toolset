<%inherit file="base.mako"/>

<%block name="body_content">
<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h1>DL Data Report</h1>
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
  % for index, file in enumerate(files):
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
          <a href="files/${index}.html">Link to File Report</a>
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

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h2>Data Groups</h2>
    <table class="table table-hover">
    % for index, group in enumerate(groups):
      <tr>
        <td>${group.group}</td>
        <td>
          <a href="groups/${index}.html">Link to Group Report</a>
        </td>
      </tr>
    % endfor
    </table>
  </div>
  <div class='col-md-1'></div>
</div>

</%block>
