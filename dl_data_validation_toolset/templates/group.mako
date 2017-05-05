<%inherit file="base.mako"/>
<%block name="body_content">

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <div class="row"><h1>Group Report:</h1></div>
    <div class="row"><h1>${report.group}</h1></div>
    <div class="row"><h2>Directory: ${report.dir}</h2></div>  
  </div>
  <div class='col-md-1'></div>
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
  <h2>Files</h2>
  <table class="table table-hover">
    <tr>
    <th>Name</th>
    </tr>
  % for _file in report.files:
      <tr>
        <td>
        <p class="text-primary">
          ${_file}
        </p>
        </td>
      </tr>
    % endfor
    </table>
  </div>
  <div class='col-md-1'></div>
</div>


</%block>