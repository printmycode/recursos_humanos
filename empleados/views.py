from django.shortcuts import render, redirect
from empleados.models import Employee
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from empleados.forms import EmployeeFilterForm
from django.contrib.auth import authenticate, login

# Create your views here.
# def login(request):
#     return redirect('/')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, '/', {'error_message': 'Usuario o constraseña incorrectos'})
    
    return redirect('/') 

def base(request):
    return render(request, 'base.html')

# Por si ingresa el filtro de gender en español
def convertir_genero(genero_texto):
    if genero_texto.lower() in ['hombre', 'male']:
        return "M"
    elif genero_texto.lower() in ['mujer', 'female']:
        return "F"
    else:
        return genero_texto

# Vista para lista de empleados en pagina de inicio y filtro según variables de businessentityid, jobtitle y gender
def lista_empleados(request):    
    # Obtener datos del formulario
    form = EmployeeFilterForm(request.GET)
    
    try:
        # Validar formulario
        if form.is_valid():
            
            # Obtener parámetros para filtrar
            businessentityid = request.GET.get('businessentityid', '')
            jobtitle = request.GET.get('jobtitle', '')
            gender = request.GET.get('gender', '')
    
            # Para filtrar por M o F si ingresan Male Female
            gender = convertir_genero(gender)
            
            empleados = Employee.objects.all()
            
            # Obtener el ID como un número
            if businessentityid.isdigit():
                businessentityid = int(businessentityid)
                empleados = empleados.filter(businessentityid=businessentityid)
            
            if jobtitle:
                empleados = empleados.filter(jobtitle__icontains=jobtitle)

            if gender:
                empleados = empleados.filter(gender__iexact=gender)
                
        else:
            # Mostrar todos los empleados si el formulario no es válido
            empleados = Employee.objects.all()
    
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        # No mostrar ni un empleado si ocurre un error
        empleados = Employee.objects.none()
        
    paginate_by = request.GET.get('paginate_by', 290)
    paginator = Paginator(empleados, paginate_by)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    mensaje_bienvenida = None
    boton_login_logout = "Login"

    if request.user.is_authenticated:
        mensaje_bienvenida = f"Hola, {request.user.username}"
        boton_login_logout = "Logout"
        
    context = {
        'empleados': empleados, 
        'page': page, 
        'form': form,
        'mensaje_bienvenida': mensaje_bienvenida,
        'boton_login_logout' : boton_login_logout,
    }

    return render(request, 'lista_empleados.html', context)