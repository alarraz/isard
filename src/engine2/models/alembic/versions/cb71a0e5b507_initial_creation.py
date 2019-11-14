"""Initial creation

Revision ID: cb71a0e5b507
Revises: 
Create Date: 2019-11-07 19:20:01.517946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from models.base_mixin import BaseMixin
from models.domain import *
from models.snippets import XMLHelper

# ~ Base, domain, Boot, Interface, Graphic, Video, Disk, DiskBus, DiskFormat
# Iso, Floppy

Session = sessionmaker()


# revision identifiers, used by Alembic.
revision = 'cb71a0e5b507'
down_revision = None
branch_labels = None
depends_on = None

xml = XMLHelper()


    
def upgrade():
    bind = op.get_bind()
    BaseMixin.metadata.create_all(bind=bind)
    
    session = Session(bind=bind)
    
   
    ## Add virtio-install xmls 
    session.bulk_save_objects([DomainXML(name=x['name'], xml=x['xml']) for x in xml.get_virtinstalls()])
    
    ## Add snippet xmls
    session.bulk_save_objects([DiskXML(name=i['name'], xml=i['xml']) for i in xml.get_snippets('disk')])
    session.bulk_save_objects([MediaXML(name=i['name'], xml=i['xml']) for i in xml.get_snippets('media')])
    session.bulk_save_objects([InterfaceXML(name=i['name'], xml=i['xml']) for i in xml.get_snippets('interface')])
    session.bulk_save_objects([GraphicXML(name=i['name'], xml=i['xml']) for i in xml.get_snippets('graphic')])
    session.bulk_save_objects([VideoXML(name=i['name'], xml=i['xml']) for i in xml.get_snippets('video')])

    ################################3
    # New domain.
    ## Get xml for new domain
    d_xml = session.query(DomainXML).filter(DomainXML.name == 'win2k3').one()
    
    ## Create the domain
    domain = Domain(name="_admin_tetros", domain_xml=d_xml, vcpu = 1, memory = 768)

    ### Boot
    db = Boot(domain_id=domain.id, name='BOOT_PXE') #, order=1)
    domain.boot.append(db)
    db = Boot(domain_id=domain.id, name='BOOT_HD') #, order=1)
    domain.boot.append(db)
    db = Boot(domain_id=domain.id, name='BOOT_CD') #, order=1)
    domain.boot.append(db)
    

    # ~ print(Boot.filter_by(name='disk').first())
    ### Hard disk
    dd_xml = session.query(DiskXML).filter(DiskXML.name == 'disk').one()
    dd = Disk(domain_id=domain.id, xml=dd_xml, name='_admin_tetros', rpath='admin/admin', bus='virtio', dev='vda', size=10, format='qcow2', order=1)
    domain.disk.append(dd)

    ### Medias
    dm_xml = session.query(MediaXML).filter(MediaXML.name == 'iso').one()
    dm = Disk(domain_id=domain.id, xml=dd_xml, name='_admin_tetros', rpath='admin/admin', bus='virtio', dev='vda', size=10, format='qcow2', order=1)
    domain.disk.append(dd)
    
    ### Interfaces
    di_xml = session.query(InterfaceXML).filter(InterfaceXML.name == 'network').one()
    di = Domain_Interface(domain_id=domain, interface_id=di_xml.id, order=1)
    domain.interfaces.append(di)        
        
    ### Graphics
    dg_xml = session.query(GraphicXML).filter(GraphicXML.name == 'spice').one()
    dg = Domain_Graphic(domain_id=domain, graphic_id=dg_xml.id, order=1)
    domain.graphic.append(dg)
    
    ### Videos
    dv_xml = session.query(VideoXML).filter(VideoXML.name == 'qxl').one()
    dv = Domain_Video(domain_id=domain, video_id=dv_xml.id, order=1)
    domain.videos.append(dv)
    
    
    
    
    
        
    session.add(domain)  
    
    # ~ print(session.query(Boot).filter(Boot.name == 'disk').one())
    # ~ exit(1)
    # ~ domain.boot.remove(session.query(Boot).filter(Boot.name == 'disk').one()) 
    
    # ~ session.commit()
    # ~ session = Session(bind=bind)
    # ~ db = Boot(domain_id=domain.id, name='disk')
    # ~ try: 
        # ~ domain.boot.insert(1,db)
    # ~ except Exception as IntegrityError:
        # ~ domain.boot.remove(session.query(Boot).filter(Boot.name == 'disk').one()) 
        # ~ domain.boot.insert(1,db)
    
    domain.boot.append(db)
    # ~ domain.boot.reorder()        
    session.commit()

    # ~ print(Domain.get_xml("_amin_tetros"))

def downgrade():
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind)
    # ~ for tbl in reversed(Base.metadata.sorted_tables):
        # ~ engine.execute(tbl.delete())
