import {
  Datagrid,
  DateField,
  NumberField,
  ReferenceManyField,
  SelectField,
  Show,
  SimpleShowLayout,
  TextField,
} from "react-admin";
import { PackingListStatusChoices } from "../values/packing-list-status-choices";

export const PackingListShow = () => (
  <Show>
    <SimpleShowLayout>
      <TextField source="documentNumber" />
      <NumberField source="totalItems" />
      <SelectField source="status" choices={PackingListStatusChoices} />
      <DateField source="receivedDate" showTime />
      <TextField source="shipToGLN" label="Ship to GLN" />
      <TextField source="shipToName" />
      <TextField source="shipToAddressLine1" />
      <TextField source="shipToAddressLine2" />
      <TextField source="shipToCity" />
      <TextField source="shipToCountryCode" />
      <TextField source="shipToPostalCode" />
      <ReferenceManyField
        reference="package"
        target="packingListId"
        label="Packages"
      >
        <Datagrid bulkActionButtons={false}>
          <TextField source="packageNumber" />
          <TextField source="SSCC" label="SSCC" />
          <NumberField source="width" />
          <NumberField source="length" />
          <NumberField source="height" />
          <NumberField source="weight" />
        </Datagrid>
      </ReferenceManyField>
    </SimpleShowLayout>
  </Show>
);
