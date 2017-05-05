<%inherit file="base.mako"/>

<%block name="body_content">


<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
    <h1>File Report For: ${report.filename}</h1>
    <h3>Directory: ${report.parent} <h3>
    </div>
  <div class='col-md-1'></div>    
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
%if report.valid :
      <h2><span class="label label-success"> Valid</span></h2>
%else:
      <h2><span class="label label-danger"> Invalid</span></h2>
%endif
    </div>
  <div class='col-md-1'></div>    
</div>

<div class="row">
  <div class='col-md-1'></div>
  <div class="col-md-10">
  <h2>Test Results</h2>
  <table class="table table-hover">
    <tr>
    <th>Name</th><th>Passed</th><th>Extras</th>
    </tr>
  % for result in report.reports:
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


</%block>