	function setQuotaOptions(parentid){
        api.ajax('/hardware','GET','').done(function(hardware) {
            user=hardware.user
            parentid=parentid+' ';
				$(parentid+"#quota-domains-desktops").ionRangeSlider({
						  type: "single",
						  min: 1,
						  max: user['quota-domains-desktops'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");
				$(parentid+"#quota-domains-running").ionRangeSlider({
						  type: "single",
						  min: 1,
						  max: user['quota-domains-running'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");	
				$(parentid+"#quota-domains-templates").ionRangeSlider({
						  type: "single",
						  min: 0,
						  max: user['quota-domains-templates'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");		
				$(parentid+"#quota-domains-isos").ionRangeSlider({
						  type: "single",
						  min: 0,
						  max: user['quota-domains-isos'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");	
				$(parentid+"#quota-hardware-memory").ionRangeSlider({
						  type: "single",
						  min: 1000,
						  max: user['quota-hardware-memory']/1000,
                          step: 250,
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");
				$(parentid+"#quota-hardware-vcpus").ionRangeSlider({
						  type: "single",
						  min: 1,
						  max: user['quota-hardware-vcpus'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");	
        });
    }; 

    function quota2dict(data){
         data['quota']={'hardware':{},'domains':{}}
         hwids=['vcpus','memory']
		 $.each(hwids,function(idx,id){
            delete data['quota-hardware-'+id];
            data['quota']['hardware'][id]=parseInt($('#quota-hardware-'+id).val())  || 0
         });
         
         dmids=['desktops','running','templates','isos']
		 $.each(dmids,function(idx,id){
            delete data['quota-domains-'+id];
            data['quota']['domains'][id]=parseInt($('#quota-domains-'+id).val())  || 0
         });         
        return data
    }

	function setQuotaTableDefaults(div_id,table,id){
			api.ajax('/admin/tabletest/'+table+'/post','POST',{'id':id}).done(function(domain) {
				$(div_id+" #quota-domains-desktops").data("ionRangeSlider").update({
						  from: domain['quota-domains-desktops']
                });
				$(div_id+" #quota-domains-running").data("ionRangeSlider").update({
						  from: domain['quota-domains-running']
                });
                $(div_id+" #quota-domains-templates").data("ionRangeSlider").update({
						  from: domain['quota-domains-templates']
                });
				$(div_id+" #quota-domains-isos").data("ionRangeSlider").update({
						  from: domain['quota-domains-isos']
                });                

				$(div_id+" #quota-hardware-memory").data("ionRangeSlider").update({
						  from: domain['quota-hardware-memory']/1000
                });
				$(div_id+" #quota-hardware-vcpus").data("ionRangeSlider").update({
						  from: domain['quota-hardware-vcpus']
                });
					  
			}); 
	}


